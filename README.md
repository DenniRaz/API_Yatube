# api_final

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/DenniRaz/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Использованные технологии:

```
Django REST Framework
```

Примеры запросов к API:

POST-запрос

```
http://127.0.0.1:8000/api/v1/jwt/create/
```

Request samples

```
{
    "username": "string",
    "password": "string"
}
```

GET-запрос

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

Response samples

```
[
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "created": "2019-08-24T14:15:22Z",
        "post": 0
    }
]
```