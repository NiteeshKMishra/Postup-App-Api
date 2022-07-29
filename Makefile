help:
	@egrep "^# target:" [Mm]akefile

create-app:
	docker-compose run --rm app sh -c "django-admin startproject $(app) ."

build:
	docker-compose build

lint:
	docker-compose run --rm app sh -c "flake8"

run:
	docker-compose up

down:
	docker-compose down