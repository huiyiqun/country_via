import csv
import requests
import itertools

from netaddr import cidr_merge, iprange_to_cidrs
from ipaddress import (summarize_address_range,
                       collapse_addresses, IPv4Address)

class AddressBlock(object):
    def __init__(self, country_code):
        self.country_code = country_code

    @property
    def blocks(self):
        if not hasattr(self, '_block'):
            res = requests.get(
                'http://www.nirsoft.net/countryip/{}.csv'.format(self.country_code))
            raw_blocks = [row.split(',') for row in res.text.split('\r\n') if row]
            self._blocks = [{'start': row[0], 'end': row[1]} for row in raw_blocks]

        return self._blocks

    @property
    def networks(self):
        if not hasattr(self, '_networks'):
            self._networks = collapse_addresses(
                itertools.chain(*[summarize_address_range(
                    IPv4Address(block['start']),
                    IPv4Address(block['end'])) for block in self.blocks]))
        return self._networks



if __name__ == '__main__':
    for network in AddressBlock('cn').networks:
        print(network.with_prefixlen)
