from setuptools import setup

setup(
    name = 'scraper',
    author='Jane Tan',
    url='https://github.com/xueyingtan/WebScrapingTute',
    version = '0.1.0',
    entry_points = {
        'console_scripts': [
            'scrape = scraper:main'
        ]
    },
    python_requires=">=3.8",
    license="MIT"
)
