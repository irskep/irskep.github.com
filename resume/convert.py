#!/usr/bin/env python
import sys
from argparse import RawDescriptionHelpFormatter
from collections import namedtuple
from xml.dom import minidom

import attr
import jinja2
from html5print import HTMLBeautifier


@attr.s
class Entry:
  title = attr.ib(default=None)
  subtitle = attr.ib(default=None)
  year_start = attr.ib(default=None)
  year_end = attr.ib(default=None)
  url = attr.ib(default=None)
  description = attr.ib(default=None)

def main():
  work_history = []
  personal_projects = []
  education = []

  current_entry = None

  with open('template.html', 'r') as f:
    template = f.read()

  doc = minidom.parse(sys.argv[1])
  body = doc.getElementsByTagName('body')[0]

  # uglyhtml = body.toxml('UTF-8').decode('UTF-8')
  # prettyhtml = HTMLBeautifier.beautify(uglyhtml, 2)
  # print(prettyhtml)

  body_div = body.childNodes[0]

  mode = 'WORK HISTORY'
  for child in body_div.childNodes:
    if mode == 'WORK HISTORY':
      if child.tagName == 'p' and child.attributes['class'].value == 'p3':
        title = child.childNodes[0].childNodes[0].data.strip()
        years = child.childNodes[2].childNodes[0].data.strip()
        year_start, year_end = (None, None)
        if '-' in years:
          (year_start, year_end) = years.split('&ndash;')
        else:
          year_start = year_end = years
        # print('Start', title)
        current_entry = Entry(
          title=title,
          year_start=year_start,
          year_end=year_end or 'Present')
        work_history.append(current_entry)
      elif child.attributes['class'].value == 'p4':
        current_entry.subtitle = child.childNodes[0].data.strip()
      elif child.attributes['class'].value == 'p5':
        current_entry.description = child.childNodes[0].data.strip()
        # print(current_entry)
      elif child.tagName == 'h1' and child.attributes['class'].value == 'p2' and child.childNodes[0].data.strip() == 'Personal Projects':
        mode = 'PERSONAL PROJECTS'
        current_entry = None

    elif mode == 'PERSONAL PROJECTS':
      if child.tagName == 'p' and child.attributes['class'].value == 'p6':
        title = child.childNodes[0].childNodes[0].childNodes[0].data.strip()
        meta = child.childNodes[2].childNodes[0].childNodes[0].data.strip()
        if meta.startswith('('):
          url = None
          year = meta[1:-1]
        else:
          (url, year) = meta.split('(')
          year = year[:-1] # remove parens
          url = url.strip()
        # print('Start', title)
        current_entry = Entry(
          title=title,
          year_start=year,
          year_end=year,
          url=url)
        personal_projects.append(current_entry)
      elif child.attributes['class'].value == 'p5':
        if current_entry.description:
          current_entry.description += '<br>'
          current_entry.description += child.childNodes[0].data.strip()
        else:
          current_entry.description = child.childNodes[0].data.strip()
        # print(current_entry)
      elif child.tagName == 'h1' and child.attributes['class'].value == 'p2' and child.childNodes[0].data.strip() == 'Education':
        mode = 'EDUCATION'
        current_entry = None

    elif mode == 'EDUCATION':
      if child.tagName == 'p' and child.attributes['class'].value == 'p6':
        title = child.childNodes[0].childNodes[0].childNodes[0].data.strip()
        years = child.childNodes[2].childNodes[0].childNodes[0].data.strip()
        year_start, year_end = (None, None)
        print(repr(years))
        (year_start, year_end) = years.split('–')
        # print('Start', title)
        current_entry = Entry(
          title=title,
          year_start=year_start,
          year_end=year_end)
        education.append(current_entry)
      elif child.attributes['class'].value == 'p5':
        if current_entry.description:
          current_entry.description += '<br>'
          current_entry.description += child.childNodes[0].data.strip()
        else:
          current_entry.description = child.childNodes[0].data.strip()
        # print(current_entry)
      elif child.tagName == 'h1' and child.attributes['class'].value == 'p2' and child.childNodes[0].data.strip() == 'Education':
        mode = 'EDUCATION'
        current_entry = None

  with open(sys.argv[2], 'w') as f:
    f.write(jinja2.Template(template).render(
      work_history=work_history,
      personal_projects=personal_projects,
      education=education))

  """
  del body.attributes['onload']

  # strip style from div.body
  for el in doc.getElementsByTagName('div'):
    try:
      if el.attributes['class'].value == 'body':
        del el.attributes['style']
    except KeyError:
      continue

  # replace garbage span with useful div
  for el in doc.getElementsByTagName('span'):
    try:
      if el.attributes['style'].value.startswith('float:right'):
        # replace img with useful info
        print("go")
        print(el.childNodes[0])
        del el.attributes['style']
        el.tagName = 'div'
        classAttr = doc.createAttribute('class')
        classAttr.value = 'contact'
        el.attributes['class']  = classAttr
    except KeyError:
      continue

  # strip empty styles for readability
  for tag_name in ('p', 'div', 'h1', 'h2', 'h3', 'h4', 'h5'):
    for el in doc.getElementsByTagName(tag_name):
      try:
        if not el.attributes['style'].value:
          del el.attributes['style']
      except KeyError:
        pass

  uglyhtml = body.toxml('UTF-8').decode('UTF-8')
  """

main()