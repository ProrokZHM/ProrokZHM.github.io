# Голос Экономики — официальный сайт

Статический сайт на русском языке. Исходники сайта отделены от Android-приложения. Сборка не требует зависимостей и платных сервисов.

## Локальная проверка

```sh
python build.py
python tests/check_site.py
python -m http.server 8000 --directory dist
```

Страницы: `/`, `/app/`, `/about/`, `/contacts/`, `/privacy/`. Файлы РСЯ лежат в `dist/` и публикуются в корне хостинга. SHA-256 оригиналов: `app-ads.txt` — `93a6e859acb5c5c7124f6bacb1194ae81a5b4a3fdb65e50abf6fe79125dffecd`; `ads.txt` — `913c5dfdfe179295cd76c3c54dd20ccba1e2077438a9c60d09cc3a91a94861d6`.

## GitHub Pages

Исходники размещены в отдельном **публичном** репозитории `ProrokZHM/ProrokZHM.github.io`. GitHub Pages публикует ветку `main` из корня; `build.py` зеркалирует содержимое `dist/` в корень. Workflow `.github/workflows/pages.yml` проверяет сборку, ссылки, политику и хэши РСЯ. Не переносите в репозиторий Android-код или ключ подписи.

После публикации проверьте `https://economevoice.ru/app-ads.txt` и `/ads.txt`: HTTPS 200, `text/plain`, SHA-256 как выше. Адрес сайта разработчика в RuStore меняется отдельно, после подтверждения сайта владельцем.

## economevoice.ru

Владелец зарегистрировал `economevoice.ru` в Рег.ру до 27.11.2027 и поручил подключить именно его. `economvoice.ru` — другое, не купленное имя. В GitHub Pages укажите `economevoice.ru` как Custom domain. В DNS Рег.ру задайте четыре A-записи для `@` на `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` и CNAME для `www` на `prorokzhm.github.io`; сверяйте адреса с [текущей документацией GitHub Pages](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site). После выпуска сертификата включите Enforce HTTPS и проверьте страницы и оба файла РСЯ.

## Источники

Политика в `source/privacy-v3.html` перенесена из опубликованной версии Sites v3 от 26.11.2026. Логотип взят из исходников приложения; внешние площадки сверены с `MainActivity.java`. Карточка RuStore не добавлена до проверки её публичного URL.
