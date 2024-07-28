import argparse
import os
import pathlib
import re

import markdown
import jinja2
from markupsafe import Markup
import yaml

data_dir = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))

OUTPUTS = [
    ("html_template.html", "resume.html"),
]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("-f", "--file", default=str(data_dir / "resume.yaml"))
    p.add_argument("-o", "--output", default=str(data_dir / "resume.typst"))

    args = p.parse_args()

    in_path = pathlib.Path(args.file)

    with in_path.open("r") as f:
        data = yaml.safe_load(f)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(str(data_dir)))
    env.filters["comma_list"] = comma_list
    env.filters["date_range"] = date_range
    env.filters["md"] = md

    for i in range(4):
        write_html(i + 1, 4, data, env)


def write_html(n, total, data, env):
    def filename(nn):
        if nn == 1:
            return "resume.html"
        else:
            return f"resume{nn}.html"

    with (data_dir / f"theme{n}.css").open("r") as f:
        css = f.read()

    prev_url = None
    next_url = None
    if n > 1:
        prev_url = filename(n - 1)
    if n < total:
        next_url = filename(n + 1)

    result = env.get_template("html_template.html").render(
        css=css, next_url=next_url, prev_url=prev_url, total=total, n=n, **data
    )
    with (data_dir / filename(n)).open("w") as f:
        f.write(result)


LINK_RE = re.compile(r'\<a href="([^"]+)"\>(.*?)\</a\>')


def date_range(s):
    en_dash = "–"
    if s["startDate"] == s["endDate"]:
        return s["startDate"]
    else:
        return f'{s["startDate"]}{en_dash}{s["endDate"]}'


def md(s):
    return Markup(markdown.markdown(s))


def comma_list(vals):
    return ", ".join(vals)


if __name__ == "__main__":
    main()
