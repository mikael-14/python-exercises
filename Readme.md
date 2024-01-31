# About

This repository contains exercises in python, for review and some reference about this programming language.

## Start a project in python 

1. Generate python sandbox (virtual environment). The . is the folder for dependencies
```
python3 -m venv .
```
2. Activate the virtual environment (linux is source command)
```
source bin/activate 
```
3. Install the dependencies inside the virtual environment (-r recursive)
```
pip install -r requirements.txt
```
4. For lock the dependencies inside the file
```
pip freeze > requirements.txt
```

## Django

```
pip install django 

django-admin startproject <project-name>
```

### Run server
cd to <project-name>

```
python3 manage.py runserver <port>
```
### Generate migrations
```
python3 manage.py makemigrations
```

### Run migrations

```
python3 manage.py migrate
```

### Create a new super user
```
python3 manage.py createsuperuser
```
### Create a new module app
```
python3 manage.py startapp <module-app>
```
After this command this gonna create a new folder, and inside this folder we have models.py for manipulate model and database table. After add to the list INSTALLED_APPS in settings.py
To this module show in admin we have to register in the admin.py 

Inside the settings.py we have project configurations

| Variable | Description |
| :- | :- |
| `DEBUG` | Debug mode |
| `ALLOWED_HOSTS` | List for alowed host. For all internet '0.0.0.0' and for everything he can use '*' |
| `INSTALLED_APPS` | After we create a new module we have to register here |
| `MIDDLEWARE` | All middleware from this app |
| `TEMPLATES` | Register templates. To add custom folder we add this to the dictionary: <br> 'DIRS': [os.path.join(BASE_DIR,'templates')],<br> 'APP_DIRS': True, |

Simple explanation bellow 

| File | Description |
| :- | :- |
| `urls.py` | Prject setting: Where we register our routes |
| :- | :- |
| `admin.py` | For registing models to display in admin section on Django. Example:<br> `class ContactoAdmin(admin.ModelAdmin):` <br> `list_display = ('nome', 'numero_telefone', 'morada')` <br> `admin.site.register(Contacto, ContactoAdmin)` |
| `apps.py` | Set configs for this module. Example: <br> `class GestaoContactosConfig(AppConfig):` <br> `default_auto_field = 'django.db.models.BigAutoField'` <br> `name = 'gestao_contactos'` |
| `models.py` | Set models, to connect to an table in database. Example: <br>`class Contacto(models.Model):`<br>`nome = models.CharField(max_length=100)` <br>`numero_telefone = models.CharField(max_length=100,primary_key=True)`<br>`morada = models.CharField(max_length=100)` |
| `serializer.py` | For converting into Python data types into JSON or other content types (it's great for api) |
| `tests.py` | To create test |
| `views.py` | To define the views. We can return a simple response or sending to a template with data |

## Django Rest Framework

Install this after installing django 
```
pip install djangorestframework
pip install markdown 
pip install django-filter
```
Add in settings.py in INSTALLED_APPS the 'rest_framework' module