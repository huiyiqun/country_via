import argparse
from ipaddress import ip_network

from country_via.renderer import Renderer
from country_via.nirsoft import CountryAddressBlock

def parse_args(*args, **kwargs):
    parser = argparse.ArgumentParser(
        description='Generate route for given country')

    addresses_group = parser.add_mutually_exclusive_group(required=True)
    addresses_group.add_argument('--country', '-c', help='fetch addresses from nirsoft with the country code',
                                 dest='country_code')
    addresses_group.add_argument('--file', help='read addresses from plain text',
                                 dest='file')

    variables_group = parser.add_argument_group('variables for the template')
    variables_group.add_argument('--via', '-v', help='the gateway for the country',
                                 dest='via')
    variables_group.add_argument('--dev', '-d', help='the device name of gateway',
                                 dest='dev')
    variables_group.add_argument('--type', '-t', help='the routing type',
                                 dest='type')
    variables_group.add_argument('--table', help='the routing table number to be operated',
                                 dest='table')

    parser.add_argument('--format', '-f', help='the format of the output', default='ip_route',
                        choices=['ip_route', 'systemd_network', 'plain_list'], dest='format')
    return parser.parse_args(*args, **kwargs)


def country_via():
    args = parse_args()

    if args.country_code:
        networks = CountryAddressBlock(args.country_code).networks
    else:
        # from file
        with open(args.file) as f:
            networks = list(map(ip_network, (addr for addr in f.read().splitlines() if addr)))

    renderer = Renderer(networks, {
        'via': args.via,
        'dev': args.dev,
        'type': args.type,
        'table': args.table,
    })
    print(renderer.render(args.format))
