#!/usr/bin/env python
import json
import sys
import jinja2


def main():
  with open('template.html', 'r') as f:
    template = f.read()

  total = int(sys.argv[1])
  n = int(sys.argv[2])

  with open(sys.argv[3], 'r') as f:
    data = json.loads(f.read())

  with open(sys.argv[4], 'r') as f:
    css = f.read()

  prev_url = None
  next_url = None
  if n > 1:
    prev_url = 'resume{}.html'.format(n - 1)
  if n < total:
    next_url = 'resume{}.html'.format(n + 1)

  if prev_url == 'resume1.html':
    prev_url = 'resume.html'

  with open(sys.argv[5], 'w') as f:
    f.write(jinja2.Template(template).render(
      css=css,
      next_url=next_url,
      prev_url=prev_url,
      total=total,
      n=n,
      **data))

if __name__ == '__main__':
  main()