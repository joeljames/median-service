.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"

	@echo "  test            Runs unit tests and coverage."

.PHONY: test
test:
	@bin/test
