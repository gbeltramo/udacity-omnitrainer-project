.PHONY: build install install-editable test

build:
	uv run python -m build -v .

install:
	uv run pip install --no-deps --force-reinstall dist/*.whl

install-editable:
	uv run pip install --no-deps --force-reinstall --verbose --editable .

test:
	uv run pytest -v -rP tests/

style:
	uv run ruff format .
	uv run ruff check --fix .
