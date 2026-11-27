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

После публикации проверьте `https://prorokzhm.github.io/app-ads.txt` и `/ads.txt`: HTTPS 200, `text/plain`, SHA-256 как выше. Адрес сайта разработчика в RuStore меняется отдельно, после подтверждения сайта владельцем.

## economvoice.ru

Домен пока не подключён. При наличии подтверждённого владения и доступа к DNS: добавьте домен в Settings → Pages → Custom domain, внесите DNS-записи по текущей [документации GitHub Pages](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), дождитесь HTTPS и включите Enforce HTTPS. После проверки замените `ORIGIN` в `build.py`, пересоберите сайт и снова проверьте ссылки, sitemap, canonical и файлы РСЯ. Регистрация или продление `.ru` домена может требовать оплаты; этот проект не совершает платежей.

## Источники

Политика в `source/privacy-v3.html` перенесена из опубликованной версии Sites v3 от 26.11.2026. Логотип взят из исходников приложения; внешние площадки сверены с `MainActivity.java`. Карточка RuStore не добавлена до проверки её публичного URL.
