
from setuptools import setup

setup(
    name='SornaMusicScraper',
    version='0.1.0',
    description='scrap https://sornamusic.ir/',
    author='rf_luj',
    packages=['sornamusicscraper'],
    requires=['bs4', 'requests']
)
