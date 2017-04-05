#!/usr/bin/python

"""
Part of this work is based on Google Python IP address manipulation library (https://code.google.com/p/ipaddr-py/) 
and Jeff Ferland IPy library (https://github.com/autocracy/python-ipy).

You need either ipaddr or IPy; versions >=0.2 of this library try to import ipaddr, then fall back on IPy.

pip install ipaddr
pip install IPy

Then you need to install pakage ipdetails from:

https://github.com/pierky/ipdetailscache

git clone https://github.com/pierky/ipdetailscache.git
python setup.py build
python setup.py install

then you ready to use it
Usage ./ipdetails.py 8.8.8.8

"""
from pierky.ipdetailscache import IPDetailsCache
import sys

IPADD= sys.argv[1]

cache = IPDetailsCache( IP_ADDRESSES_CACHE_FILE = "ip_addr.cache", IP_PREFIXES_CACHE_FILE = "ip_pref.cache", MAX_CACHE = 604800, Debug = False )
cache.UseIXPs( WhenUse=1, IXP_CACHE_FILE="ixps.cache", MAX_CACHE=604800 )
result = cache.GetIPInformation( IPADD )
