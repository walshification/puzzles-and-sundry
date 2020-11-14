test: lint test-unit

fmt:
	pipenv run black .

lint:
	pipenv run black . --check
	pipenv run flake8

test-unit:
	pipenv run pytest

clean:
	pipenv clean
