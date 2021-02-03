from setuptools import setup

setup(
    name = 'scraper',
    version = '0.1.0',
    entry_points = {
        'console_scripts': [
            'scrape = scraper:main'
        ]
    })