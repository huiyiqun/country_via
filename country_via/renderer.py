from country_via.nirsoft import AddressBlock
from jinja2 import Environment, PackageLoader


class Renderer:
    def __init__(self, country_code, via, dev=None):
        self.country_networks = AddressBlock(country_code).networks
        self.env = Environment(loader=PackageLoader('country_via'))
        self.env.globals['via'] = via
        self.env.globals['country_networks'] = self.country_networks
        if dev is not None:
            self.env.globals['dev'] = dev

    def render(self, template):
        return self.env.get_template(template+'.j2').render()


if __name__ == '__main__':
    renderer = Renderer('cn', '10.233.0.2', 'eth0')
    print(renderer.render('ip_route'))
