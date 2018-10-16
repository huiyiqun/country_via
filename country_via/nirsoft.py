import requests

from ipaddress import (summarize_address_range,
                       collapse_addresses, IPv4Address)


class CountryAddressBlock:
    def __init__(self, country_code):
        self.country_code = country_code

    @property
    def blocks(self):
        if not hasattr(self, '_blocks'):
            blocks = []
            res = requests.get(
                'http://www.nirsoft.net/countryip/{}.csv'.format(
                    self.country_code))
            for row in res.text.split('\r\n'):
                if row:
                    raw_block = row.split(',')
                    blocks.append({
                        'start': raw_block[0],
                        'end': raw_block[1]
                    })
            self._blocks = blocks
        return self._blocks

    @property
    def networks(self):
        if not hasattr(self, '_networks'):
            self._networks = []
            for i, block in enumerate(self.blocks):
                self._networks += summarize_address_range(
                    IPv4Address(block['start']),
                    IPv4Address(block['end']))
            self._networks = list(collapse_addresses(self._networks))
        return self._networks


if __name__ == '__main__':
    for network in CountryAddressBlock('cn').networks:
        print(network.with_prefixlen)
    print(len(CountryAddressBlock('cn').networks))
