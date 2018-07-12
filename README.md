# Simple Blog Application powered by Django

## Required
Docker (http://docker.com).

## Build & run
`docker-compose build`

`docker-compose up`

## API root

Open `localhost:8000` in browser

## Available URLs
GET `/api/v1/users` - list of user (admin access required)

GET `/api/v1/articles` - list of current user's articles

GET `/api/v1/article/<id>` - article details

POST `/api/v1/article` - add article

## Administration panel
Default superuser is defined in `docker-compose.yml`

`localhost:8000/admin` - admin panel
