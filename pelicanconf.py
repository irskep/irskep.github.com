#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from collections import namedtuple
import sys
sys.path.append('.')

PLUGINS = [
    'minchin.pelican.plugins.summary',
]

STATIC_PATHS = [
    'img', 'downloads', 'css', 'js', 'css/style.css', 'CNAME',
    'rogue_basement_post',
]

AUTHOR = u'Steve Landey'
SITENAME = u"Steve Landey"
SITEURL = 'http://localhost:8000'

DEFAULT_CATEGORY = 'Articles'

TIMEZONE = 'US/Pacific'
DEFAULT_LANG = u'en'
DATE_FORMATS = {
    'en': '%B %-d, %Y',
}

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/all.rss.xml'

HEADER_LINKS = [
    ('Email', 'mailto:randos@steve.steveasleep.com'),
    ('GitHub', 'https://github.com/irskep'),
    ('Bandcamp', 'https://slamjamsen.bandcamp.com'),
    ('itch.io', 'https://irskep.itch.io'),
    # ('Twitter', 'https://twitter.com/irskep'),
    ('last.fm', 'https://www.last.fm/user/irskep'),
]

Project = namedtuple('Project', ('name', 'desc', 'img'))

"""
PROJECTS = [
    Project('Dr. Hallervorden', '7-day roguelike', None),
    Project('Sendimals', 'iMessage app for silly art', None),
    Project('Literally Canvas', 'MacPaint in JavaScript as a library', None),
    Project('Games', '', None),
]
"""

MENUITEMS = (
    ('Writing', [
        ('Blog', 'https://blog.steveasleep.com/'),
        ('Twitter', 'https://twitter.com/irskep'),
        # ('Pyglet tutorial', '/pyglettutorial.html'),
        ('Résumé', '/resume.html'),
        # ('Game jam CV', '/game-jam-cv.html'),
    ]),
    ('Games', [
        ('All games', '/games.html'),
        ('Dr. Hallervorden', 'https://irskep.itch.io/dr-hallervorden'),
        ('Power-Q', 'https://irskep.itch.io/powerq'),
        ('Rogue Basement', 'https://irskep.itch.io/roguebasement'),
    ]),
    ('Apps', [
        ('Sendimals', 'http://sendimals.com'),
        ('Asana', 'https://itunes.apple.com/us/app/asana-organize-tasks-work/id489969512?mt=8'),
    ]),
    ('Open Source', [
        ('Drawsana', 'https://asana.github.io/Drawsana/'),
        ('Literally Canvas', 'http://literallycanvas.com/'),
        ('clubsandwich', 'http://steveasleep.com.com/clubsandwich'),
        ('BearLibTerminal-Swift', 'http://steveasleep.com/BearLibTerminal-Swift/'),
        ('Jumbo Grove', 'http://steveasleep.com/jumbogrove'),
        ('sphinx-better-theme', 'https://sphinx-better-theme.readthedocs.io/en/latest/'),
    ]),
    # ('Music', [
        # ('The Nest', 'http://thenestmusic.com'),
        # ('Slam Jamsen', 'http://slamjamsen.com'),
    # ]),
)

DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = 200

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

TYPOGRIFY = False
TYPOGRIFY_IGNORE_TAGS = ['pre', 'code', 'head']

THEME = 'theme'
