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
