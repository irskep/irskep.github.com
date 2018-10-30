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
    'rogue_basement_post', 'rexpaint_manual.html',
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
    ('YouTube', 'https://www.youtube.com/channel/UC0lx9IhbHiM5XTcdISqttWQ'),
    ('Bandcamp', 'https://slamjamsen.bandcamp.com'),
    ('itch.io', 'https://irskep.itch.io'),
    # ('Twitter', 'https://twitter.com/irskep'),
    # ('last.fm', 'https://www.last.fm/user/irskep'),
]

Project = namedtuple('Project', ('name', 'desc', 'img'))

MENUITEMS = (
    ('Writing', [
        ('Blog', 'https://blog.steveasleep.com/', None),
        ('Twitter', 'https://twitter.com/irskep', None),
        ('Old blog', '/articles/', None),
        # ('Pyglet tutorial', '/pyglettutorial.html'),
        ('Résumé', '/resume.html', None),
        # ('Game jam CV', '/game-jam-cv.html'),
    ]),
    ('Games', [
        ('Dr. Hallervorden', 'https://irskep.itch.io/dr-hallervorden', 'dr_hallervorden.png'),
        ('Power-Q', 'https://irskep.itch.io/powerq', 'powerq.png'),
        ('Rogue Basement', 'https://irskep.itch.io/roguebasement', 'rogue_basement.png'),
        ('17 more games', '/games.html', 'gw0rp.png'),
    ]),
    ('Apps', [
        ('Sendimals', 'http://sendimals.com', 'sendimals.png'),
        ('Hipmunk', 'https://itunes.apple.com/us/app/hipmunk-travel-search/id419950680?mt=8', 'hipmunk.jpg'),
        ('Asana', 'https://itunes.apple.com/us/app/asana-organize-tasks-work/id489969512?mt=8', 'asana.jpg'),
    ]),
    ('Open Source', [
        ('Drawsana', 'https://asana.github.io/Drawsana/', None),
        ('Literally Canvas', 'http://literallycanvas.com/', None),
        ('clubsandwich', 'http://steveasleep.com/clubsandwich', None),
        ('BearLibTerminal-Swift', 'http://steveasleep.com/BearLibTerminal-Swift/', None),
        ('Jumbo Grove', 'http://steveasleep.com/jumbogrove', None),
        ('sphinx-better-theme', 'https://sphinx-better-theme.readthedocs.io/en/latest/', None),
    ]),
    # ('Music', [
        # ('The Nest', 'http://thenestmusic.com'),
        # ('Slam Jamsen', 'http://slamjamsen.com'),
    # ]),
)

CUSTOM_DESCRIPTIONS = {
    'Drawsana': "a Swift library for adding drawing and image markup features to iOS apps",
    'Literally Canvas': "a JavaScript library for adding drawing and image markup features to web pages",
    'clubsandwich': "a Python library for making roguelikes",
    'BearLibTerminal-Swift': "a Swift library for making roguelikes",
    'Jumbo Grove': "a JavaScript library for making interactive fiction games",
    'sphinx-better-theme': "a nice-looking, CSS-tweakable template for <a href=\"http://sphinx-doc.org\">Sphinx</a>",
}

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

INDEX_SAVE_AS = 'index_old.html'

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
TYPOGRIFY_IGNORE_TAGS = ['pre', 'code', 'head', 'title']

THEME = 'theme'

JINJA_FILTERS = {
    'to_css_class': lambda s: s.lower().replace(' ', ''),
    'inline': lambda s: open(s).read()
}

EXTRA_TEMPLATE_PATHS = [
    'output/css/style.css',
]