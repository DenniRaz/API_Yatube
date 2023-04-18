# Проект API для Yatube
API Yatube для проекта социальной сети Yatube.

## Описание проекта:
API Yatube социальной сети, в которой пользователи могут публиковать посты и
просматривать сообщения других пользователей. Реализованы механизм комментариев
к записям, возможность подписки на публикации интересующий авторов, регистрация
пользователей. Для аутентификации используется JWT-токен.

## Стек технологий:
* [Python 3.7](https://www.python.org/downloads/)
* [Django 2.2.16](https://www.djangoproject.com/download/)
* [Django Rest Framework 3.12.4](https://pypi.org/project/djangorestframework/#files)
* [Pytest 6.2.4](https://pypi.org/project/pytest/)
* [Simple-JWT 1.7.2](https://pypi.org/project/djangorestframework-simplejwt/)

## Как запустить проект:

* Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:DenniRaz/API_Yatube.git
```
```
cd yatube_api
```

* Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
```
venv/scripts/activate
```

* Установить зависимости из файла ```requirements.txt```:
```
pip install -r requirements.txt
```

* Выполнить миграции:
```
python manage.py migrate
```

* Запустить проект:
```
python manage.py runserver
```

## Документация для Yatube API доступна по адресу:
```http://127.0.0.1/redoc/```