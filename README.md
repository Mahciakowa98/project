# project
# Ecommerce - web application (Python - Django, JavaScript, HTML, CSS)

A web application created using the Django framework - shirt online store

## Technologies used

- Python
- Django
- JavaScript

## Python modules

- asgiref
- boto3
- botocore
- Django
- django-allow-cidr
- django-crispy-forms
- django-mathfilters
- django-utils-six
- gunicorn
- jmespath
- packaging
- Pillow
- pyparsing
- python-dateutil
- s3transfer
- six
- sqlparse
- tzdata
- urllib3

## Installation

To start working with the project you need to install the framework [Django](https://docs.djangoproject.com/en/4.1/):

```bash
python -m pip install Django
```

Clone project to your computer:

```bash
git clone https://github.com/Mahciakowa98/project.git
```

Make sure you have installed virtualenv and you have created your virtual environment:

```bash
pip install virtualenv
```


Next - upload the file requirements.txt:

```bash
pip install -r requirements.txt
```
Migrate project:

```bash
python manage.py migrate
```

After successful migration you can run the project on your lockalhost:
```bash
python manage.py runserver
```
