# Django web app - display repo commits

## Exercise description
Une petite appli (1 page) Django qui affiche la liste des derniers commit d'un repo github (ou Bitbucket en fonction de ta préférence) en fonction de son nom.

il faut donc
- un champs de recherche où on peut écrire le nom du repo github,
- un bouton "Submit" pour lancer la recherche
- une liste qui affiche les commits avec le message, l'id et la date du commit

## Requirements

### Python

Python already installed in Windows env with path set in Windows PATH:
C:\Program Files\Python38

Python version:
```
>python --version
Python 3.8.2
```

### Pip

Pip already installed in Windows env with path set in Windows PATH:
C:\Program Files\Python38\Scripts

Pip version:
```
>python -m pip --version
pip 20.1.1
```

### Django

Django official release installation from Windows cmd:
```
>python -m pip install Django 
```

Django version:
```
>python -m django --version
3.0.8
```


## Django project

### Project creation
Go to install directory and use the following command:
```
>django-admin startproject qwarrysiteproject
```
Creation of this project tree:
```
.
+-- qwarrysiteproject/
|   +-- manage.py
|   +-- qwarrysiteproject/
|   |   +-- __init__.py
|   |   +-- settings.py
|   |   +-- urls.py
|   |   +-- asgi.py
|   |   +-- wsgi.py
```

### Application Creation
* Go to qwarrysiteproject project at manage.py level and use:
```
>python manage.py startapp githubcommits
```
* Creation of app tree:
```
.
+-- qwarrysiteproject/
|   +-- manage.py
|   +-- githubcommits/
|   |   +-- __init__.py
|   |   +-- admin.py
|   |   +-- apps.py
|   |   +-- models.py
|   |   +-- tests.py
|   |   +-- views.py
|   +-- migrations/
|   |   +-- __init__.py
|   +-- qwarrysiteproject/
|   |   +-- __init__.py
|   |   +-- settings.py
|   |   +-- urls.py
|   |   +-- asgi.py
|   |   +-- wsgi.py
```

* Update settings:
Add githubcommits app in INSTALLED_APPS. It includes actives django apps.
```
INSTALLED_APPS = [
    'githubcommits.apps.GithubcommitsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

* Project urls:
Link to apps url
```
path('githubcommits/', include('githubcommits.urls'))
```

* Template Creation:
Creation of templates directory including githubcommits and an index.html file.
```
+-- githubcommits/
|   +-- templates/
|   |   +-- githubcommits/
|   |   |   +-- index.html
```

* View Creation:
Add app intelligence and call specified pages.
   * Libraries: github from PyGithub package and django.shortcuts
   * methods: github_caller and process

Application urls:
Redirection urls to desired views.
```
from . import views

app_name = 'githubcommits'
urlpatterns = [
    path('', views.index, name='index'),
    path('process/', views.process, name='process'),
]
```


### PyGithub package and objects

Link to documentation:
<https://pygithub.readthedocs.io/en/latest/github_objects.html>
