.PHONY: help install test test-verbose clean lint format

# Default target
help:
	@echo "Available commands:"
	@echo "  install     - Install dependencies"
	@echo "  test        - Run all tests"
	@echo "  test-verbose - Run tests with verbose output"
	@echo "  clean       - Clean up generated files"
	@echo "  lint        - Run code linting"
	@echo "  format      - Format code"

install:
	pip install -r requirements.txt

test:
	behave

test-verbose:
	behave -v

test-dry:
	behave --dry-run

clean:
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf reports/
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete

lint:
	flake8 features/

format:
	black features/