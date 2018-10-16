import argparse

from country_via.renderer import Renderer


def parse_args(*args, **kwargs):
    parser = argparse.ArgumentParser(
        description='Generate route for given country')

    parser.add_argument('--country', '-c', help='country code of the destination',
                        required=True, dest='country_code')

    variables_group = parser.add_argument_group('variables')
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
    renderer = Renderer(args.country_code, {
        'via': args.via,
        'dev': args.dev,
        'type': args.type,
        'table': args.table,
    })
    print(renderer.render(args.format))
