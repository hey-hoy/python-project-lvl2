gendiff:
	poetry run gendiff $(ARGS)

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install dist/hexlet_code-0.1.0-py3-none-any.whl --force-reinstall

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

.PHONY: gendiff install test lint selfcheck check build
