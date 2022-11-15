# Django YouTube Downloader 
---

## Instalation

Clone repo: 
```console
$ git clone https://github.com/Dasifue/YouTubeDowloader.git
```

Install requirements:
```console
$ pip install -r requirements.txt
```

Go to file ***venv\Lib\site-packages\pafy\backend_youtube_dl.py*** and change **53, 54** rows:
```
self._likes = 0
self._dislikes = 0
```

Migrations:
```console
$ python manage.py migrate
```

Go to ***main*** folder and create **tg_bot_token.py**:
```
# inside the file
TOKEN = "Your bot token"
```
---
## Running:

Run **web**:

```console
$ python manage.py runserver
```

Run **TelegramBot**:

```console
$ python manage.py bot
```
---