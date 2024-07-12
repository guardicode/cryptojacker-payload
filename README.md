# Cryptojacker Payload - Agent Plugin for Infection Monkey

## Introduction

Cryptojacker Payload is an Agent Plugin for
[Infection Monkey](https://www.akamai.com/infectionmonkey) that
can simulate the behavior of a cryptojacker. The plugin will use the
CPU and memory of infected systems to perform cryptographic operations.
It can also imitate bitcoin mining network traffic by sending
network requests.

For more information, see the [Cryptojacker Payload Plugin
documentation](https://techdocs.akamai.com/infection-monkey/docs/cryptojacker-simulation).

## Development
### Setting up the development environment

To create the resulting Cryptojacker archive, follow these steps:

1. **Clone the Repository**

    ```sh
    $ git clone https://github.com/guardicode/cryptojacker-payload.git
    $ cd cryptojacker-payload
    ```

1. **Install development dependencies**

    This project uses [Poetry](https://python-poetry.org/) for managing
    dependencies and virtual environments, and
    [pre-commit](https://pre-commit.com/) for managing pre-commit hooks.

    ```sh
    $ pip install pre-commit poetry
    $ pre-commit install -t pre-commit
    $ poetry install
    ```

### Running the test suite

The test suite can be run with the following command:

```sh
poetry run pytest
```

### Building the plugin

To build the plugin, run the [Agent Plugin
Builder](https://github.com/guardicode/agent-plugin-builder/).

```sh
poetry run build_agent_plugin .
```

The build tool will create `Cryptojacker-payload.tar`, which can be [installed in
the Monkey Island](https://techdocs.akamai.com/infection-monkey/docs/plugins).
