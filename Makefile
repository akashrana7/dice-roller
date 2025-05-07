# Makefile for dice-roller project

.PHONY: help test bump release format pre-commit

help:
	@echo "Common tasks:"
	@echo "  make test         - Run test suite with pytest"
	@echo "  make bump         - Bump version using Commitizen (requires .cz.yaml)"
	@echo "  make release      - Push version tag and trigger CI release"
	@echo "  make format       - Auto-format code with black"
	@echo "  make pre-commit   - Install pre-commit hooks"

test:
	pytest

bump:
	cz bump

release:
	git push && git push --tags

format:
	black .

pre-commit:
	pre-commit install
