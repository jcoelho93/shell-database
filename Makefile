.PHONY: tests clean

clean:
	rm -rf *.egg-info __pycache__ .pytest_cache

tests:
	python3.8 -m poetry run pytest
