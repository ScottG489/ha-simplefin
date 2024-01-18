# ha-simplefin
![maintenance-status](https://img.shields.io/badge/maintenance-active-brightgreen)

SimpleFIN integration for Home Assistant.

## Features
- 

### Planned features
- 


## Installation
First add this repository [as a custom repository](https://hacs.xyz/docs/faq/custom_repositories/).

### Setup
#### Prerequisites


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

### Troubleshooting
