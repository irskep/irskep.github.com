# -*- encoding: utf-8 -*-
"""
Markdown extension that inserts &shy; entities (soft hyphens) into words based
on the hyphenation dictionary. Requires the Hyphenator library.
"""
import re

from hyphenator import Hyphenator
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

WORD_RE = re.compile(r'\b(?P<word>\w+)\b')

h = Hyphenator('hyph_en_US.dic')


def hyphenate(m):
    word = m.group('word')
    positions = set(h.positions(word))
    characters = []
    for i, char in enumerate(word):
        if i in positions:
            characters.append('&shy;')
        characters.append(char)
    return ''.join(characters)


class HyphenProcessor(Preprocessor):
    def run(self, lines):
        return [WORD_RE.sub(hyphenate, line) for line in lines]


class HyphenExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add('hyphen', HyphenProcessor(md), '_begin')
        md.registerExtension(self)
