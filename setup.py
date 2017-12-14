#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'CoinMarketCapWrapper',
    version = '1.0.0',
    url = 'https://github.com/iJEEBUS/CoinMarketCapWrapper',
    download_url = 'https://github.com/iJEEBUS/CoinMarketCapWrapper/archive/master.zip',
    author = 'Ronald Rounsifer : ronrounsifer@me.com',
    author_email = 'ronrounsifer@me.com',
    license = 'MIT',
    packages = ['CoinMarketCapWrapper'],
    description = 'Python wrapper for coinmarketcap.com API.',
    long_description = open('README.md','r').read(),
    install_requires=['requests', 'json'],
    keywords = ['cryptocurrency', 'API', 'coinmarketcap','BTC', 'Bitcoin', 'LTC', 'Litecoin', 'DOGE', 'Dogecoin', 'ETH', 'Ethereum'],
)