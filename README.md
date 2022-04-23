# CINEMA ENG

Enjoy the comfortable selection of cinema tickets to see your favorite movie

# Requirements

- docker
- docker-compose

# Use

`cp .env.example .env` and replace your environment in .env file

`docker-compose build`

`docker-compose up`

`docker-compose run app python manage.py migrate`

`docker-compose run app python manage.py createsuperuser`

`docker-compose run app python manage.py collectstatic`