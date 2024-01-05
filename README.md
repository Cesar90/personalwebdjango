# PersonalWebDjango

Project based on django with docker

# Build project with docker-compose

docker-compose build

# Create django project

docker-compose run --rm app sh -c "django-admin startproject app ."

# Show packages installed

docker-compose run --rm app sh -c "pip list"

# Create core app

docker-compose run --rm app sh -c "python manage.py startapp core"