# Simple Blog Application powered by Django

# Required

Python 3

## Set up
`pip install django`
`pip install djangorestframework`
`python manage.py migrate`

## How to run
`python manage.py runserver`
open `localhost:8000/api/v1/articles` in browser

## Available URLs
GET `/api/v1/articles` - list of articles
GET `/api/v1/article/<id>` - article details
POST `/api/v1/article` - add article

## Administration panel
`python manage.py createsuperuser` - set up admin username and password
`localhost:8000/admin` - admin panel
