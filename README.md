# Country Via

Naive Scripts to help you manage routes to specific country.

## Installation

```
~> pip install country-via
```

## Usage

```
~> country-via --help
usage: country-via [-h] (--country COUNTRY_CODE | --file FILE) [--via VIA]
                   [--dev DEV] [--type TYPE] [--table TABLE]
                   [--format {ip_route,systemd_network,plain_list}]

Generate route for given country

optional arguments:
  -h, --help            show this help message and exit
  --country COUNTRY_CODE, -c COUNTRY_CODE
                        fetch addresses from nirsoft with the country code
  --file FILE           read addresses from plain text
  --format {ip_route,systemd_network,plain_list}, -f {ip_route,systemd_network,plain_list}
                        the format of the output

variables for the template:
  --via VIA, -v VIA     the gateway for the country
  --dev DEV, -d DEV     the device name of gateway
  --type TYPE, -t TYPE  the routing type
  --table TABLE         the routing table number to be operated
```

## Examples

To dump networks of China:

```
~> country-via --country cn --format plain_list
```

To set up routes for China with [systemd-networkd](https://github.com/systemd/systemd):

```
~> country-via --country cn --format systemd_network --via 10.233.0.1 > /etc/systemd/network/ol.network.d/cn.conf
```

To set up routes for China on the fly (with [iproute2](https://github.com/shemminger/iproute2)):

```
~> country-via --country cn --format systemd_network --via 10.233.0.1 | sudo bash
```

To set up routes table for custom addresses:

```
~> country-via --file campus.txt --format systemd_network --via 10.233.0.1 > /etc/systemd/network/ol.network.d/campus.conf
```
