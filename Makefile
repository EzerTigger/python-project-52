dev:
	poetry run python3 manage.py runserver
shell:
	poetry run python3 manage.py shell_plus
install:
	poetry install
migrate:
	poetry run python3 ./manage.py migrate
superuser:
	poetry run python3 ./manage.py createsuperuser --no-input
build: install migrate superuser
