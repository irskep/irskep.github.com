#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys
sys.path.append('.')

STATIC_PATHS = ['img', 'downloads', 'css', 'js', 'css/style.css', 'CNAME']

AUTHOR = u'Steve Johnson'
SITENAME = u"Steve Johnson’s Web Presence"
SITEURL = 'http://localhost:8000'

DEFAULT_CATEGORY = 'Blog'

TIMEZONE = 'US/Pacific'
DEFAULT_LANG = u'en'
DATE_FORMATS = {
    'en': '%d %b %Y',
}

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/all.rss.xml'

MENUITEMS = (
    ('Read me', '/'),
    ('Games', '/games.html'),
    ('Open source', '/open-source.html'),
    ('Pyglet tutorial', '/pyglettutorial.html'),
    ('The Nest', 'http://thenestmusic.com'),
)

DEFAULT_PAGINATION = False

ARTICLE_PATHS = [
    'posts'
]

# this always has to be .html so /pyglettutorial.html doesn't break
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL

ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL

CATEGORY_URL = '{slug}'
CATEGORY_SAVE_AS = '%s/index.html' % CATEGORY_URL
TAG_URL = '{slug}'
TAG_SAVE_AS = '%s/index.html' % TAG_URL
MD_EXTENSIONS = [
    'codehilite(css_class=highlight)', 'extra', 'sane_lists', 'toc',
    ]

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_PAGINATION = False

TYPOGRIFY = True

THEME = 'theme'
