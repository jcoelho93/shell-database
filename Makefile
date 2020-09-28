.PHONY: tests clean

clean:
	rm -rf *.egg-info __pycache__ .pytest_cache .coverage

install-deps:
	python3.8 -m pip install -r requirements.txt

install-dev-deps:
	python3.8 -m pip install -r dev-requirements.txt

install: install-deps
	python3.8 -m pip install .

uninstall:
	python3.8 -m pip uninstall .

tests:
	python3.8 -m poetry run pytest
