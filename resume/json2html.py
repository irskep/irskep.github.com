#!/usr/bin/env python
import json
import sys
import jinja2


def main():
  with open('template.html', 'r') as f:
    template = f.read()

  with open(sys.argv[1], 'r') as f:
    data = json.loads(f.read())

  with open(sys.argv[2], 'r') as f:
    css = f.read()

  with open(sys.argv[3], 'w') as f:
    f.write(jinja2.Template(template).render(css=css, **data))

if __name__ == '__main__':
  main()