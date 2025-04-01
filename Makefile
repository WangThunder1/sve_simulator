install:
	pip install pip-tools
	pip install -r requirements.txt
	pre-commit install
	git config blame.ignoreRevsFile .git-blame-ignore-revs

migrate:
	python manage.py migrate

start:
	python manage.py runserver

