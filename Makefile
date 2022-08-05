all: build

# Installs all of the necessary python requirements.
setup:
	pip install -r requirements.txt

# Builds the entire static site documentation.
build: validate
	mdbook build
	python scripts/openapi-build.py --input-file vic.api.v0.yaml --output-dir public --output-name vic.api.v0
	python scripts/openapi-build.py --input-file vic.api.v1.yaml --output-dir public --output-name vic.api.v1

# Cleans the entire project of generated files.
clean:
	rm -rf public
	rm -f src/vic.api.v0.html
	rm -f src/vic.api.v1.html

# Runs validations for the openapi specs
validate:
	python -m openapi_spec_validator vic.api.v1.yaml
	python -m openapi_spec_validator vic.api.v0.yaml
