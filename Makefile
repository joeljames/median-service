.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"

	@echo "  test            Runs unit tests and coverage."
	@echo "  seed_db         Reseed the database."
	@echo "  lint            Lint all project files."

.PHONY: test
test:
	@bin/test

.PHONY: seed_db
seed_db:
	@bin/seed_db


.PHONY: lint
lint:
	@bin/lint
