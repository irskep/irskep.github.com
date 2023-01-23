#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from collections import namedtuple
import sys

sys.path.append(".")

PLUGINS = [
    "minchin.pelican.plugins.summary",
    "minify",
]

MINIFY = {
    "remove_comments": True,
}

STATIC_PATHS = [
    "img",
    "downloads",
    "css",
    "js",
    "css/style.css",
    "CNAME",
    "rexpaint_manual.html",
]

AUTHOR = "Steve Landey"
SITENAME = "Steve Landey"
SITEURL = "http://localhost:8001"

DEFAULT_CATEGORY = "Articles"

TIMEZONE = "US/Pacific"
DEFAULT_LANG = "en"
DATE_FORMATS = {
    "en": "%B %-d, %Y",
}

# Feed generation is usually not desired when developing
FEED_ALL_RSS = "feeds/all.rss.xml"

HEADER_LINKS = [
    ("Email", "mailto:randos@steve.steveasleep.com"),
    ("GitHub", "https://github.com/irskep"),
    ("YouTube", "https://www.youtube.com/channel/UC0lx9IhbHiM5XTcdISqttWQ"),
    ("Bandcamp", "https://slamjamsen.bandcamp.com"),
    ("itch.io", "https://irskep.itch.io"),
    # ('Twitter', 'https://twitter.com/irskep'),
    # ('last.fm', 'https://www.last.fm/user/irskep'),
]

Project = namedtuple("Project", ("name", "desc", "img"))

MENUITEMS = (
    (
        "Writing",
        [
            ("Blog", "https://blog.steveasleep.com/", None),
            ("Mastodon", "https://mastodon.gamedev.place/@irskep", None),
            ("Old blog", "/articles/", None),
            # ('Pyglet tutorial', '/pyglettutorial.html'),
            ("Résumé", "/resume.html", None),
            ("Why you'd want to hire me", "https://periodic-patio-e0c.notion.site/Why-you-d-want-to-hire-me-a2acc41e9928470994640911831dc990", None),
            # ('Game jam CV', '/game-jam-cv.html'),
        ],
    ),
    (
        "Games",
        [
            (
                "Vigil@nte",
                "https://irskep.itch.io/vigilante",
                "vigilante.png",
            ),
            (
                "Dr. Hallervorden",
                "https://irskep.itch.io/dr-hallervorden",
                "dr_hallervorden.png",
            ),
            ("Power-Q", "https://irskep.itch.io/powerq", "powerq.png"),
            (
                "Rogue Basement",
                "https://irskep.itch.io/roguebasement",
                "rogue_basement.png",
            ),
            ("17 more games", "/games.html", "gw0rp.png"),
        ],
    ),
    (
        "Apps",
        [
            ("Oscillator Drum Jams", "https://oscillatordrums.com", "oscillator.png"),
            ("Sendimals", "http://sendimals.com", "sendimals.png"),
            (
                "Hipmunk",
                "https://blog.steveasleep.com/my-time-at-hipmunk",
                "hipmunk.jpg",
            ),
            (
                "Asana",
                "https://itunes.apple.com/us/app/asana-organize-tasks-work/id489969512?mt=8",
                "asana.jpg",
            ),
        ],
    ),
    (
        "Other good stuff",
        [
            ("Browserboard", "https://browserboard.com", None),
            ("Steve’s Pedal Shop", "https://steveasleep.com/pedalshop/", None),
            ("Keplverse", "https://steveasleep.com/keplverse/", None),
            ("Locheck", "https://github.com/Asana/locheck", None),
            ("Literally Canvas", "http://literallycanvas.com/", None),
            ("clubsandwich", "https://steveasleep.com/clubsandwich", None),
            (
                "BearLibTerminal-Swift",
                "https://steveasleep.com/BearLibTerminal-Swift/",
                None,
            ),
            # ('Jumbo Grove', 'https://steveasleep.com/jumbogrove', None),
            (
                "sphinx-better-theme",
                "https://sphinx-better-theme.readthedocs.io/en/latest/",
                None,
            ),
        ],
    ),
    # ('Music', [
    # ('The Nest', 'http://thenestmusic.com'),
    # ('Slam Jamsen', 'http://slamjamsen.com'),
    # ]),
)

CUSTOM_DESCRIPTIONS = {
    "Browserboard": "a multiuser online whiteboard",
    "Keplverse": "a scientifically accurate procedural star system generator",
    "Drawsana": "a Swift library for adding drawing and image markup features to iOS apps",
    "Literally Canvas": "a JavaScript library for adding drawing and image markup features to web pages",
    "Locheck": "a localization validator for iOS and Android",
    "clubsandwich": "a Python library for making roguelikes",
    "BearLibTerminal-Swift": "a Swift library for making roguelikes",
    "Jumbo Grove": "a JavaScript library for making interactive fiction games",
    "Steve’s Pedal Shop": "a procedural guitar pedal generator",
    "sphinx-better-theme": 'a nice-looking, CSS-tweakable template for <a href="http://sphinx-doc.org">Sphinx</a>',
}

DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = 200

ARTICLE_PATHS = ["posts"]

# this always has to be .html so /pyglettutorial.html doesn't break
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = PAGE_URL

ARTICLE_URL = "{slug}.html"
ARTICLE_SAVE_AS = ARTICLE_URL

INDEX_SAVE_AS = "index_old.html"

CATEGORY_URL = "{slug}"
CATEGORY_SAVE_AS = "%s/index.html" % CATEGORY_URL
TAG_URL = "{slug}"
TAG_SAVE_AS = "%s/index.html" % TAG_URL
MD_EXTENSIONS = [
    "codehilite(css_class=highlight)",
    "extra",
    "sane_lists",
    "toc",
]

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_PAGINATION = False

TYPOGRIFY = True
TYPOGRIFY_IGNORE_TAGS = ["pre", "code", "head", "title"]

THEME = "theme"


def inline_fn(s):
    try:
        return open(s).read()
    except FileNotFoundError:
        return open("content/" + s).read()


JINJA_FILTERS = {
    "to_css_class": lambda s: s.lower().replace(" ", ""),
    "inline": inline_fn,
}

