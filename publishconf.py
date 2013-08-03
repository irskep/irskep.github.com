#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://steveasleep.com'
SITEURL = 'http://steveasleep.com/beta'
RELATIVE_URLS = False

FEED_ALL_RSS = 'feeds/all.rss.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "UA-4517625-1"

MENUITEMS = [
    (a, SITEURL + b if b.startswith('/') else b)
    for a, b in MENUITEMS
]
