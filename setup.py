from setuptools import setup

setup(
    name="country_via",
    version="0.0.1",
    description="Route Configuring Tool for Country",
    author="Hui Yiqun",
    author_email="huiyiqun@gmail.com",
    license='MIT',
    url="https://github.com/huiyiqun/country_via",
    packages=["country_via"],
    install_requires=[
        'requests',
        'jinja2',
    ]
)
