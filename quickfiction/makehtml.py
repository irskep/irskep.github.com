#!/usr/bin/env python
import json
import os
import sys
import jinja2


def main():
  with open('template.html', 'r') as f:
    template = f.read()

  total = 1
  while os.path.exists('theme{}.css'.format(total + 1)):
    total += 1

  for n in range(1, total + 1):
    with open('theme{}.css'.format(n)) as f:
      css = f.read()

    prev_url = None
    next_url = None
    if n > 1:
      prev_url = 'index{}.html'.format(n - 1) if n > 2 else 'index.html'
    if n < total:
      next_url = 'index{}.html'.format(n + 1)

    out_path = 'index{}.html'.format(n) if n > 1 else 'index.html'

    with open(out_path, 'w') as f:
      f.write(jinja2.Template(template).render(
        css=css,
        next_url=next_url,
        prev_url=prev_url,
        total=total,
        n=n))

if __name__ == '__main__':
  main()