# CINEMA ENG

Enjoy the comfortable selection of cinema tickets to see your favorite movie

## Requirements

- docker
- docker-compose

## Use

`cp .env.example .env` and replace your environment in .env file

`docker-compose build`

`docker-compose up`

`docker-compose run app python manage.py migrate`

`docker-compose run app python manage.py createsuperuser`

`docker-compose run app python manage.py collectstatic`

**website:**
 - 127.0.0.1:8000

**admin panel:**
- 127.0.0.1:8000/admin

**endpoins:**
- 127.0.0.1:8000/api/v1/program/update/{pk}
- 127.0.0.1:8000/api/v1/chair/update/{pk}
- 127.0.0.1:8000/api/v1/movie/get/
- 127.0.0.1:8000/api/v1/movie/get/{pk}
- 127.0.0.1:8000/api/v1/movie/delete/{pk}
- 127.0.0.1:8000/api/v1/movie/update/{pk}
- 127.0.0.1:8000/api/v1/movie/post/
- 127.0.0.1:8000/api/v1/cinemaroom/get/
- 127.0.0.1:8000/api/v1/cinemaroom/get/{pk}
- 127.0.0.1:8000/api/v1/cinemaroom/delete/{pk}
- 127.0.0.1:8000/api/v1/cinemaroom/update/{pk}
- 127.0.0.1:8000/api/v1/cinemaroom/post/
 

<br>

## Licnese

[GNU](https://github.com/lampesm/cinema-eng/blob/main/LICENSE)