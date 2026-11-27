from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import re

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
HASHES = {
    'app-ads.txt': '93a6e859acb5c5c7124f6bacb1194ae81a5b4a3fdb65e50abf6fe79125dffecd',
    'ads.txt': '913c5dfdfe179295cd76c3c54dd20ccba1e2077438a9c60d09cc3a91a94861d6',
}
class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.h1=0; self.lang=False
    def handle_starttag(self, tag, attrs):
        data=dict(attrs)
        if tag=='html': self.lang=data.get('lang')=='ru'
        if tag=='h1': self.h1+=1
        for key in ('href','src'):
            if key in data: self.links.append(data[key])

for name, expected in HASHES.items():
    value=(DIST/name).read_bytes()
    actual=sha256(value).hexdigest()
    assert actual==expected,(name,actual)
assert b'yandex.com, 335400201, DIRECT' in (DIST/'app-ads.txt').read_bytes()

pages=['index.html','app/index.html','about/index.html','contacts/index.html','privacy/index.html','404.html']
for name in pages:
    text=(DIST/name).read_text(encoding='utf-8')
    parser=Links();parser.feed(text)
    assert parser.lang and parser.h1==1,name
    assert '<meta name="description"' in text and '<link rel="canonical"' in text,name
    for link in parser.links:
        if link.startswith(('mailto:','https://','#')): continue
        assert link.startswith('/'),(name,link)
        target=DIST/link.lstrip('/')
        if link.endswith('/'): target=target/'index.html'
        assert target.exists(),(name,link)
    assert 'economvoice.ru' not in text,name

source=(ROOT/'source/privacy-v3.html').read_text(encoding='utf-8')
policy=(DIST/'privacy/index.html').read_text(encoding='utf-8')
body=re.search(r'(<section>.*?</footer>)',source).group(1).split('<footer>')[0]
assert body in policy,'Current Sites v3 policy body changed'
assert (DIST/'robots.txt').exists() and (DIST/'sitemap.xml').exists()
print(f'PASS: {len(pages)} pages, local links, policy v3, advertising file hashes')
