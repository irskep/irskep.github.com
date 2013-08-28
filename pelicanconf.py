#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys
sys.path.append('.')

STATIC_PATHS = ['img', 'downloads', 'css', 'js']
FILES_TO_COPY = (
    ('css/style.css', 'css/style.css'),
    ('CNAME', 'CNAME'),
)

AUTHOR = u'Steve Johnson'
SITENAME = u"Steve Johnson’s Partial Creative Output"
SITEURL = 'http://localhost:8000'

DEFAULT_CATEGORY = 'Blog'

TIMEZONE = 'US/Pacific'
DEFAULT_LANG = u'en'
DATE_FORMATS = {
    'en': '%d %b %Y',
}

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/all.rss.xml'

# Blogroll
LINKS = (('The Buildy Blog', 'http://blog.playbuildy.com/'),)

# Social widget
SOCIAL = (
    ('Twitter', 'http://twitter.com/irskep'),
    ('Stack Overflow', 'http://stackoverflow.com/users/8061/steve-johnson'),
    ('LinkedIn', 'http://www.linkedin.com/pub/steve-johnson/11/900/567'),
)
TWITTER_USERNAME = 'irskep'

MENUITEMS = (
    ('Articles', '/'),
    ('Side Channel', '/side-channel'),
    ('Games', '/games.html'),
    ('Open Source', '/open-source.html'),
    ('Pyglet tutorial', '/pyglettutorial.html'),
)

DEFAULT_PAGINATION = False

ARTICLE_DIR = 'posts'

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

FIND_MAIN_PAGE_CATEGORY = lambda categories: [
    articles for category, articles in categories
    if category == 'Articles'
][0]
