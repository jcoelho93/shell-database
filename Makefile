.PHONY: tests clean lint install install-deps install-dev-deps uninstall build publish

clean:
	rm -rf *.egg-info __pycache__ .pytest_cache .coverage dist

install-deps:
	python3.8 -m pip install -r requirements.txt

install-dev-deps:
	python3.8 -m pip install -r dev-requirements.txt

install: install-deps
	python3.8 -m pip install .

build:
	python3.8 setup.py sdist bdist_wheel

uninstall:
	python3.8 -m pip uninstall .

tests: install-deps install-dev-deps
	python3.8 -m pytest --ignore W -v --junit-xml=test-results.xml tests/

lint: install-dev-deps
	python3.8 -m flake8 shell_database

coverage: install-deps install-dev-deps
	python3.8 -m coverage run --branch --source shell_database -m pytest -- tests
	python3.8 -m coverage xml --omit=**/__init__.py

publish: build install-dev-deps
	python3.8 -m twine check dist/*
	python3.8 -m twine upload dist/*