#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

STATIC_PATHS = ['img', 'downloads']

AUTHOR = u'Steve Johnson'
SITENAME = u"Steve Johnson's Partial Creative Output"
SITEURL = ''

DEFAULT_CATEGORY = 'Blog'

TIMEZONE = 'US/Pacific'
DEFAULT_LANG = u'en'
DATE_FORMATS = {
    'en': '%d %b %Y',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

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
    ('Games', '/games'),
    ('Open Source', '/open-source'),
    ('Pyglet tutorial', '/pyglettutorial'),
    ('The New Dork Times', 'http://steveasleep.com/newdorktimes'),
)

DEFAULT_PAGINATION = False

ARTICLE_DIR = 'posts'

ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '%s/index.html' % ARTICLE_URL
PAGE_URL = ARTICLE_URL
PAGE_SAVE_AS = '%s/index.html' % PAGE_URL
CATEGORY_URL = ARTICLE_URL
CATEGORY_SAVE_AS = '%s/index.html' % CATEGORY_URL
TAG_URL = ARTICLE_URL
TAG_SAVE_AS = '%s/index.html' % TAG_URL

TEMPLATE_PAGES = {
    '404.html': '404.html',
}

DISPLAY_PAGES_ON_MENU = False
DEFAULT_PAGINATION = False

TYPOGRIFY = True

THEME = 'theme'
