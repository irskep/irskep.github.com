#!/usr/bin/env python
import json
import re
import sys
from xml.etree import ElementTree

import attr
import jinja2
import prettyprinter
import xmljson
from html5print import HTMLBeautifier


URL_YEAR_RE = re.compile(r'((?P<url>http.+)\b )?\((?P<year>[^)]+)\)')


@attr.s
class Entry:
  title = attr.ib(default=None)
  subtitle = attr.ib(default=None)
  years = attr.ib(default=None)
  url = attr.ib(default=None)
  description = attr.ib(default=None)


@attr.s
class SimpleNode:
  tag = attr.ib()
  attributes = attr.ib()
  children = attr.ib()

  @classmethod
  def parse(cls, key, obj):
    if not isinstance(obj, dict):
      return obj
    if not obj:
      return obj
    if 'child' in obj or 'attributes' in obj:
      children = [SimpleNode.parse(*unwrap_obj(child_obj)) for child_obj in obj.get('children', [])]
      attributes = {k: v for k, v in obj.get('attributes', {}).items() if v}
    else:
      children = [SimpleNode.parse(*unwrap_obj(obj))]
      attributes = {}

    return flatten(SimpleNode(
      tag=key[len(r"{http://www.w3.org/1999/xhtml}"):],
      attributes=attributes,
      children=children))

  def child_text(self):
    return self.children[0]


def flatten(e):
  """
  Return node's first child iff:
  - This is a ``SimpleNode``
  - It has exactly one child
  - Either:
    - Its child is a string
    - It is a <bdi> node
    - It is a layout-only node, designated by a 'c1' CSS class
  """
  if not isinstance(e, SimpleNode):
    return e

  if len(e.children) != 1:
    e.children = [flatten(c) for c in e.children]
    return e

  is_style_class = e.attributes.get('class', '').startswith('c1')
  is_bdi = e.tag == 'bdi'

  if is_style_class or is_bdi or not isinstance(e.children[0], str):
    return flatten(e.children[0])

  return e


def unwrap_obj(obj):
  """
  Unwrap a single-key dict ``{k: v}`` into a tuple ``(k, v)``
  """
  if not isinstance(obj, dict):
    return (None, obj)
  try:
    assert len(list(obj.keys())) == 1
    k = list(obj.keys())[0]
    return (k, obj[k])
  except Exception as e:
    print(repr(obj))
    raise e


def find_title_index(items, text):
  return next(i for (i,v) in enumerate(items) if v.children == [text])


def main():
  prettyprinter.install_extras(['attrs'])

  with open('template.html', 'r') as f:
    template = f.read()

  with open(sys.argv[1], 'rb') as f:
    doc = ElementTree.fromstring(f.read())

  # convert heinous XML API to plain Python objects
  body = doc.find('{http://www.w3.org/1999/xhtml}body')[0]
  rawdata = xmljson.abdera.data(body)
  root = SimpleNode.parse(*unwrap_obj(rawdata))

  # ignore front matter
  root.attributes = {}
  root.children.remove(root.children[0])
  data = root.children

  # print for debugging
  # prettyprinter.cpprint(data)

  work_history_index = find_title_index(data, 'Work History')
  personal_projects_index = find_title_index(data, 'Personal Projects')
  education_index = find_title_index(data, 'Education')

  work_history_data = data[work_history_index+1:personal_projects_index]
  personal_projects_data = data[personal_projects_index+1:education_index]
  education_data = data[education_index+1:]

  def read_style_a(items, title_class='p3', subtitle_class='p4', description_class='p5'):
    e = None
    results = []
    for item in items:
      if item.attributes['class'] == title_class:
        years = str(item.children[2])
        match = URL_YEAR_RE.match(years)
        if match:
          e = Entry(
            title=item.children[0],
            years=match.group('year'),
            url=match.group('url'))
        else:
          e = Entry(title=item.children[0], years=years)
        results.append(e)
      elif item.attributes['class'] == subtitle_class:
        e.subtitle = item.child_text()
      elif item.attributes['class'] == description_class:
        if e.description:
          e.description += '<br>'
          e.description += item.child_text()
        else:
          e.description = item.child_text()
    return results

  work_history = read_style_a(work_history_data, title_class='p3')
  personal_projects = read_style_a(personal_projects_data, title_class='p6')
  education = read_style_a(education_data, title_class='p6')

  # prettyprinter.cpprint(work_history)
  # print()
  # prettyprinter.cpprint(personal_projects)
  # print()
  # prettyprinter.cpprint(education)

  with open(sys.argv[2], 'w') as f:
    f.write(jinja2.Template(template).render(
      work_history=work_history,
      personal_projects=personal_projects,
      education=education))

  return

if __name__ == '__main__':
  main()