# Sprint_7 — API-тесты Яндекс Самокат

Автотесты API учебного сервиса `https://qa-scooter.praktikum-services.ru`.

## Состав проекта

- `tests/test_courier_create.py` — создание курьера и проверки ошибок.
- `tests/test_courier_login.py` — авторизация курьера и проверки ошибок.
- `tests/test_orders.py` — создание заказа с параметризацией цвета и получение списка заказов.
- `helpers.py` — генерация уникальных данных и вспомогательные методы.
- `conftest.py` — фикстуры и очистка созданных курьеров.
- `postman/Sprint_7.postman_collection.json` — коллекция для ручной проверки запросов в Postman.
- `pytest.ini` — настройки pytest и Allure.

## Запуск

Требуется Python 3.10+.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Отчёт Allure

Установи Allure Commandline отдельно, затем:

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

Для сохранения статических файлов отчёта в проекте:

```bash
allure generate allure-results -o allure-report --clean
```

## Ручная проверка в Postman

1. Импортируй `postman/Sprint_7.postman_collection.json`.
2. Запусти запросы регистрации курьера, входа, создания заказа и получения списка заказов.
3. Для регистрации и входа используй одинаковые значения `login`/`password`; после успешной регистрации скопируй их в запрос входа.
4. Коллекция — стартовый набор ручных запросов; фактические ответы сервера проверь в Postman перед запуском автотестов.

## Git

```bash
git init
git add .
git commit -m "Add Sprint 7 API tests"
git branch -M main
git remote add origin <URL_ТВОЕГО_РЕПОЗИТОРИЯ>
git push -u origin main
```

После запуска Allure сгенерируй отчёт и добавь `allure-results/` или `allure-report/` в репозиторий, если этого требуют правила курса. Обычно `allure-results/` удобнее хранить как результаты прогона, а `allure-report/` — как готовый отчёт.
Проект готов к проверке.
