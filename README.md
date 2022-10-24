# проект: "Calendar"
___
## стек (python3.10, Django, Postgres)
___
**СТРУКТУРА ПРОЕКТА:**
```
flowchart TB
	node[diplom]
```

**ЗАПУСК:**
1) Клонировать проект, создать виртуальное окружение.
2) Установить менеджер пакетов POETRY и установить зависимости:
- pip install poetry
- poetry update
3) Создать в папке **"src"** файл ".env" и прописать в нем параметры:
+ DEBUG=False (при тестировании сервиса прописываем True)
+ SECRET_KEY=Секретный ключ
+ POSTGRES_DB=название БД
+ POSTGRES_USER=имя пользователя БД
+ POSTGRES_PASSWORD=пароль для подключения к БД
+ POSTGRES_HOST=хост размещения БД
+ POSTGRES_PORT=порт через который подключена БД
+ VK_OAUTH2_KEY=идентификационный ключ от ВК
+ VK_OAUTH2_SECRET=секретный ключ от ВК
+ BOT_TOKEN

4) Создать базу данных:
0. [ ] docker-compose up -d

5) Накатить миграции :beers::
0. [ ] python src/manage.py makemigrations
1. [ ] python src/manage.py migrate

6) Создать суперпользователя для входа в админку:
0. [ ] python src/manage.py createsuperuser

7) Запустить проект :zap::\
:white_check_mark: python src/manage.py runserver<br />
<br />
8) Запуск тестов:
:pick: python src/manage.py test src
