# Vic.ai API Documentation

This is where the API documentation for Vic resides.

Please open a Github issue if more clarification is needed for certain topics
and please open issues if you see areas that could be improved.

## Requirements

* Python
* Rust
* [mdBook](https://github.com/rust-lang/mdBook)

```
cargo install mdbook
```

Please ensure that you have the correct software versions as indicated in the `.tool-versions` file.
Consider using [asdf](https://asdf-vm.com/) to streamline this process:

```sh 
$ asdf install
```

## Setup

```sh
make setup
```

## Build

```sh
make build
```

## Viewing

To view the supplemental api documentation open the `index.html` in the
`public/` directory after building.

```sh
open public/index.html
```

To view the V0 openapi spec

```sh
open public/vic.api.v0.html
```

To view the V1 openapi spec

```sh
open public/vic.api.v1.html
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
