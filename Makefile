# Variables
PYTHON=python

.PHONY: help install install-dev lint format test clean

help:
	@echo "Useful commands:"
	@echo "  make install        - Install production dependencies"
	@echo "  make install-dev    - Install dev and prod dependencies"
	@echo "  make lint           - Run flake8 and mypy"
	@echo "  make format         - Run black and isort"
	@echo "  make test           - Run all tests with pytest and show coverage"
	@echo "  make clean          - Remove Python cache and coverage files"

install:
	pip install -r requirements.txt

install-dev: install
	pip install -r dev-requirements.txt

lint:
	flake8 .
	mypy src/

format:
	isort .
	black .

test:
	pytest --cov=src --cov-report=term-missing

clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
	rm -rf .pytest_cache .mypy_cache htmlcov .coverage

