from jinja2 import Environment, PackageLoader

class Renderer:
    def __init__(self, networks, env={}):
        self.env = Environment(loader=PackageLoader('country_via'))
        self.env.globals.update(env)
        self.env.globals['country_networks'] = networks

    def render(self, template):
        return self.env.get_template(template+'.j2').render()


if __name__ == '__main__':
    from ipaddress import ip_network
    renderer = Renderer(map(ip_network, ['127.0.0.1/32', '8.8.8.0/24']), {'via': '10.233.0.2', 'dev': 'eth0'})
    print(renderer.render('ip_route'))
