import argparse
import os
import pathlib
import re

import jinja2
import yaml

data_dir = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))

def main():
  p = argparse.ArgumentParser()
  p.add_argument("-f", "--file", default=str(data_dir / "resume.yaml"))
  p.add_argument("-o", "--output", default=str(data_dir / "resume.typst"))

  args = p.parse_args()

  in_path = pathlib.Path(args.file)
  out_path = pathlib.Path(args.output)

  with in_path.open('r') as f:
    data = yaml.safe_load(f)
  
  env = jinja2.Environment(loader=jinja2.FileSystemLoader(str(data_dir)))
  env.filters['date_range'] = date_range
  env.filters['typst_text'] = typst_text
  template = env.get_template("typst_template.jinja2")

  result = template.render(**data)

  with out_path.open('w') as f:
    f.write(result)

  
LINK_RE = re.compile(r'\<a href="([^"]+)"\>(.*?)\</a\>')
def typst_text(s):
  def link_sub(m):
    return f'#link("{m.group(1)}")[{m.group(2)}]'
  transformed_links = LINK_RE.sub(link_sub, s)
  transformed_chars = transformed_links.replace('@', r'\@')
  transformed_linebreaks = transformed_chars.replace('\n', '\n\n')
  return transformed_linebreaks.strip()

def date_range(s):
  en_dash = "–"
  if s["startDate"] == s["endDate"]:
    return s["startDate"]
  else:
    return f'{s["startDate"]}{en_dash}{s["endDate"]}'


if __name__ == "__main__":
  main()