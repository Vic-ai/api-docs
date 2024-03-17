all: build

build:
	npx --yes @redocly/cli build-docs vic.api.v0.yaml --output public/index.html

preview:
	npx --yes @redocly/cli preview-docs vic.api.v0.yaml

# Cleans the entire project of generated files.
clean:
	rm -rf public

# Runs validations for the openapi specs
validate:
	npx --yes @redocly/cli lint vic.api.v0.yaml
