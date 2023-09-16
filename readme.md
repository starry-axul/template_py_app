# Project

- python: 3.11.4
- pip: 23.2.1

# Setup

```
conda activate python3_11_4
```

## Creating a new app

Creating a new app, for instance **templates**

```sh
python manage.py startapp templates
```

creating a urls file, for example:

```py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

## Model

creating a model (for example in templates/models.py) and run affter:

```sh
python manage.py makemigrations
python manage.py migrate
```

https://docs.djangoproject.com/en/4.2/intro/tutorial01/

# Run

```
python manage.py runserver 8082
```
