import argparse
import json
import os
import pathlib
import re

import markdown
import jinja2
from markupsafe import Markup
import yaml

DATA_DIR = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))
JINJA2_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(str(DATA_DIR)))


def filter(fn):
    JINJA2_ENV.filters[fn.__name__] = fn
    return fn


def main():
    p = argparse.ArgumentParser()
    p.add_argument("-f", "--file", default=str(DATA_DIR / "resume.yaml"))
    p.add_argument("-o", "--output", default=str(DATA_DIR / "resume.html"))

    args = p.parse_args()

    in_path = pathlib.Path(args.file)
    out_path = pathlib.Path(args.output)

    with in_path.open("r") as f:
        data = yaml.safe_load(f)

    stylesheets = []
    for path in sorted((DATA_DIR / "themes").iterdir()):
        name = path.stem
        default_suffix = " - default"
        stylesheet = {"name": name, "css": path.read_text()}
        if name.endswith(default_suffix):
            name = name[: -len(default_suffix)]
            stylesheet["name"] = name
            stylesheets.insert(0, stylesheet)
        else:
            stylesheets.append(stylesheet)

    out_path.write_text(
        JINJA2_ENV.get_template("html_template.html").render(
            stylesheets=stylesheets, **data
        )
    )


@filter
def date_range(s):
    en_dash = "–"
    if s["startDate"] == s["endDate"]:
        return s["startDate"]
    else:
        return f'{s["startDate"]}{en_dash}{s["endDate"]}'


@filter
def md(s):
    return Markup(markdown.markdown(s))


@filter
def comma_list(vals):
    return ", ".join(vals)


@filter
def as_json(val):
    return Markup(json.dumps(val))


if __name__ == "__main__":
    main()
