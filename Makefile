dev:
	poetry run python3 manage.py runserver
test:
	poetry run python3 manage.py test
lint:
	poetry run flake8 task_manager --exclude migrations
shell:
	poetry run python3 manage.py shell_plus
install:
	poetry install
lock:
	poetry lock
migrate:
	poetry run python3 ./manage.py migrate
static:
	poetry run python3 ./manage.py collectstatic
start:
	poetry run gunicorn task_manager.wsgi:application
build: install migrate static
