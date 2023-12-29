dev:
	poetry run python3 manage.py runserver
test:
	poetry run python3 manage.py test
shell:
	poetry run python3 manage.py shell_plus
install:
	poetry install
migrate:
	poetry run python3 ./manage.py migrate
static:
	poetry run python3 ./manage.py collectstatic
build: install migrate static
