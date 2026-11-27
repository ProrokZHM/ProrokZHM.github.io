from hashlib import sha256
from html.parser import HTMLParser
from urllib.request import Request, urlopen

BASE = 'https://prorokzhm.github.io'
PATHS = ('/', '/app/', '/about/', '/contacts/', '/privacy/', '/assets/style.css', '/assets/logo.jpg', '/robots.txt', '/sitemap.xml')
HASHES = {'/app-ads.txt': '93a6e859acb5c5c7124f6bacb1194ae81a5b4a3fdb65e50abf6fe79125dffecd', '/ads.txt': '913c5dfdfe179295cd76c3c54dd20ccba1e2077438a9c60d09cc3a91a94861d6'}

class External(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = set()
    def handle_starttag(self, tag, attrs):
        href = dict(attrs).get('href', '')
        if href.startswith('https://') and not href.startswith(BASE):
            self.links.add(href)

def get(path):
    with urlopen(Request(BASE + path, headers={'User-Agent': 'Golos-Ekonomiki-site-check/1.0'}), timeout=20) as response:
        return response.status, response.headers.get('Content-Type', ''), response.read()

links = set()
for path in PATHS:
    status, mime, body = get(path)
    assert status == 200, (path, status)
    if path.endswith('/'):
        parser = External(); parser.feed(body.decode('utf-8'))
        links |= parser.links
    print(f'PASS {status} {path} {mime} {len(body)} bytes')
for path, expected in HASHES.items():
    status, mime, body = get(path)
    digest = sha256(body).hexdigest()
    assert status == 200 and digest == expected and mime.startswith('text/plain'), (path, status, mime, digest)
    print(f'PASS {status} {path} {mime} SHA-256 {digest}')
status, _, policy = get('/privacy/')
assert b'https://www.rustore.ru/help/legal/privacy-policy-users' in policy
assert b'https://www.rustore.ru/help/legal/privacy-policy"' not in policy
print('PASS current RuStore policy URL in published privacy page')
print('External HTTPS links:')
for link in sorted(links):
    print(link)

