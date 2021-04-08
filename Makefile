SHELL:=/bin/bash

.PHONY: clean
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf .pytest_cache
	rm -rf .cache
	rm -rvf ./*.egg-info
	rm -rf build
	rm -rf dist

.PHONY: lint
lint:
	pylint ./schleppy

.PHONY: test
test:
	py.test --verbose --color=yes --cov-report html --cov-report term --cov=schleppy test --cov-fail-under=100


.PHONY: check
check: lint test

.PHONY: build
build:
	python setup.py sdist bdist_wheel

.PHONY: push
push:
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
