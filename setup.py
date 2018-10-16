from setuptools import setup

setup(
    name="country_via",
    version="0.0.5",
    description="Route Configuring Tool for Country",
    author="Hui Yiqun",
    author_email="huiyiqun@gmail.com",
    license='MIT',
    url="https://github.com/huiyiqun/country_via",
    packages=["country_via"],
    install_requires=[
        'requests',
        'jinja2',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',

        'Intended Audience :: System Administrators',

        'Environment :: Console',
    ],
    keywords='network route',
    package_data={
        'country_via': ['templates/*.j2']
    },
    entry_points={
        'console_scripts': {
            'country-via=country_via.cli:country_via'
        }
    }
)
