# Vic.ai API Documentation

This is where the API documentation for Vic.ai resides.

Please open a Github issue if more clarification is needed for certain topics
and please open issues if you see areas that could be improved.

## Requirements

* Python
* Node

Please ensure that you have the correct software versions as indicated in the `.tool-versions` file. 

Consider using [asdf](https://asdf-vm.com/) to streamline this process:

```sh
$ asdf install
```

## Setup

```sh
make setup
```

## Preview

To view and develop the API documentation generated using redocly:

```sh
make preview
```

Open [http://localhost:8080](http://localhost:8080).

## Build

```sh
make build
```

## Deployment

The `main` branch is auto deployed when merged into.

## Contributing

We are using [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
for commit messages.

Any changes that alter the Open API spec significantly need to have a
corresponding entry in the `CHANGELOG`.

Feel free to clone and check out a branch and submit a PR for any spelling or
grammar mistakes.
