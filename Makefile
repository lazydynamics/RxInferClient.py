.PHONY: help generate-client clean test test-cov docs docs-serve docs-clean install-dev

# Colors for terminal output
ifdef NO_COLOR
GREEN  :=
YELLOW :=
WHITE  :=
RESET  :=
else
GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
RESET  := $(shell tput -Txterm sgr0)
endif

# Default target
.DEFAULT_GOAL := help

## Show help for each of the Makefile targets
help:
	@echo ''
	@echo 'RxInferClient.py Makefile ${YELLOW}targets${RESET}:'
	@echo ''
	@echo '${GREEN}Development setup:${RESET}'
	@echo '  ${YELLOW}install-dev${RESET}          Install development dependencies (required before using other commands)'
	@echo ''
	@echo '${GREEN}Client generation commands:${RESET}'
	@echo '  ${YELLOW}generate-client${RESET}      Generate Python client code from OpenAPI spec'
	@echo '  ${YELLOW}clean${RESET}                Clean generated files'
	@echo ''
	@echo '${GREEN}Testing commands:${RESET}'
	@echo '  ${YELLOW}test${RESET}                 Run tests'
	@echo '  ${YELLOW}test-cov${RESET}             Run tests with coverage report'
	@echo ''
	@echo '${GREEN}Documentation commands:${RESET}'
	@echo '  ${YELLOW}docs${RESET}                 Build the documentation (strict mode)'
	@echo '  ${YELLOW}docs-serve${RESET}           Serve documentation locally'
	@echo '  ${YELLOW}docs-clean${RESET}           Clean documentation build'
	@echo ''
	@echo '${GREEN}Help:${RESET}'
	@echo '  ${YELLOW}help${RESET}                 Show this help message'
	@echo ''
	@echo '${YELLOW}Note:${RESET} Run ${GREEN}make install-dev${RESET} first to install all required dependencies.'
	@echo '      Run it again if you modify any dependencies in pyproject.toml.'
	@echo ''

# Variables
OPENAPI_SPEC_URL := https://raw.githubusercontent.com/lazydynamics/RxInferServer/main/openapi/spec.yaml
TEMP_DIR := .temp
GENERATED_DIR := src
PKGNAME := rxinferclient

## Install development dependencies
install-dev:
	@echo "${GREEN}Installing development dependencies...${RESET}"
	@python -m pip install --upgrade pip
	@pip install -e ".[dev]"
	@echo "${GREEN}Development dependencies installed successfully!${RESET}"

## Generate Python client code
generate-client:
	@echo "${GREEN}Generating Python client code...${RESET}"
	@mkdir -p $(TEMP_DIR)
	@curl -s $(OPENAPI_SPEC_URL) -o $(TEMP_DIR)/spec.yaml
	@mkdir -p $(GENERATED_DIR)
	@docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate \
		-i /local/$(TEMP_DIR)/spec.yaml \
		-g python \
		-o /local/$(GENERATED_DIR) \
		--additional-properties=packageVersion=1.0.0 \
		--additional-properties=packageName=$(PKGNAME) \
		--additional-properties=library=asyncio \
		--additional-properties=packageUrl=https://github.com/lazydynamics/RxInferClient.py \
		--additional-properties=generateSourceCodeOnly=true
	@sed -E -i.bak "s/\[default to '([^']*)'\]/default to '\1'/g" $(GENERATED_DIR)/$(PKGNAME)/docs/*.md && rm $(GENERATED_DIR)/$(PKGNAME)/docs/*.bak
	@sed -E -i.bak "s|\(rxinferclient/docs/|\(docs/|g" $(GENERATED_DIR)/$(PKGNAME)_README.md && rm $(GENERATED_DIR)/$(PKGNAME)_README.md.bak
	@rm -rf $(TEMP_DIR)
	@echo "${GREEN}Client code generated successfully!${RESET}"

## Clean generated files
clean:
	@echo "${GREEN}Cleaning generated files...${RESET}"
	@rm -rf $(TEMP_DIR)
	@rm -rf $(GENERATED_DIR)
	@echo "${GREEN}Clean complete!${RESET}"

## Run tests
test:
	@echo "${GREEN}Running tests...${RESET}"
	@pytest tests/

## Run tests with coverage
test-cov:
	@echo "${GREEN}Running tests with coverage...${RESET}"
	@pytest --cov=rxinfer_client tests/

## Build documentation
docs:
	@echo "${GREEN}Building documentation...${RESET}"
	@mkdocs build --strict
	@echo "${GREEN}Documentation built successfully!${RESET}"

## Serve documentation locally
docs-serve:
	@echo "${GREEN}Serving documentation locally...${RESET}"
	@mkdocs serve

## Clean documentation build
docs-clean:
	@echo "${GREEN}Cleaning documentation build...${RESET}"
	@rm -rf site/
	@echo "${GREEN}Documentation build cleaned!${RESET}" 