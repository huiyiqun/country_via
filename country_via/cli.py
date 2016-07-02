import argparse

from country_via.renderer import Renderer

parser = argparse.ArgumentParser(
    description='Generate route for given country')

parser.add_argument('--country', '-c', help='country code of the destination',
                    required=True, dest='country_code')
parser.add_argument('--via', '-v', help='gateway for the country',
                    required=True, dest='via')
parser.add_argument('--dev', '-d', help='device name of gateway',
                    dest='dev')
parser.add_argument('--format', '-f', help='format of out', default='ip_route',
                    choices=['ip_route', 'systemd_network'], dest='format')


def country_via():
    args = parser.parse_args()
    renderer = Renderer(args.country_code, args.via, args.dev)
    print(renderer.render(args.format))
