# ha-simplefin
![maintenance-status](https://img.shields.io/badge/maintenance-active-brightgreen)

[SimpleFIN](https://www.simplefin.org/) integration for Home Assistant.

## Features
- Entites for balances for each of your accounts

### Planned features
- Entities for more fine-grained investment holdings
- Transaction data?

## Installation
First add this repository [as a custom repository](https://hacs.xyz/docs/faq/custom_repositories/).

### Setup
#### Prerequisites
Before setting up this integration, you need to get credentials by
[creating a SimpleFIN account](https://beta-bridge.simplefin.org/). Connect your financial institutions to the platform,
create a new "app", and record your setup token as this will need to be provided to the HA integration.

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=simplefin)


## Development
Run the following to set up your development environment
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements_test.txt
```
To run Home Assistant with this integration loaded:
```shell
hass -c config
```
### Testing
To run unit tests with coverage:
```shell
pytest tests --cov=custom_components.simplefin --cov-report term-missing
```

### Releasing
[Create a new GitHub release](https://github.com/ScottG489/ha-simplefin/releases/new). The [release workflow](https://github.com/ScottG489/ha-simplefin/blob/master/.github/workflows/release.yaml) takes care of the rest.
When finished, it will be available to download via HACS.
