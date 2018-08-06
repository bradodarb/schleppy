SHELL:=/bin/bash


.PHONY: lint
lint:
	pylint ./src

.PHONY: test
test:
	py.test --verbose --color=yes --cov-report html --cov-report term --cov=schleppy test --cov-fail-under=100


.PHONY: check
check: lint unit-test integration-test

.PHONY: build
build:
	python setup.py sdist bdist_wheel

.PHONY: push
push:
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
