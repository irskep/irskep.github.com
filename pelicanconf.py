#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

STATIC_PATHS = ['img', 'downloads']

AUTHOR = u'Steve Johnson'
SITENAME = u"Steve Johnson's Partial Creative Output"
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

ARTICLE_DIR = 'posts'

ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '%s/index.html' % ARTICLE_URL
PAGE_URL = ARTICLE_URL
PAGE_SAVE_AS = '%s/index.html' % PAGE_URL

DISPLAY_PAGES_ON_MENU = False
