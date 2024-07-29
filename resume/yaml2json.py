import argparse
import json
import os
import pathlib
import re
import yaml

DATA_DIR = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))
LINK_RE = re.compile(r'\<a href="([^"]+)"\>(.*?)\</a\>')
SPACE_RE = re.compile(r' +')
def flatten_links(s):
    return LINK_RE.sub(lambda m: m.group(1), s).replace("<br>", "")


def fix_spacing(s):
    return SPACE_RE.sub(" ", s).strip()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("-f", "--file", type=pathlib.Path)
    p.add_argument("-o", "--output", type=pathlib.Path)

    args = p.parse_args()

    data = yaml.safe_load(args.file.read_text())
    del data["appendices"]

    data["basics"]["summary"] = fix_spacing(flatten_links(data["basics"]["summary"]))

    for item in data["work"]:
        if "breakAfter" in item:
            del item["breakAfter"]
        item["summary"] = fix_spacing(item["summary"])

    for item in data["skills"]:
      if "text" in item:
          del item["text"]

    for item in data["work"] + data["projects"] + data["education"]:
        item["startDate"] = item["startDate"] + "-01-01"
        item["endDate"] = item["endDate"] + "-01-01"
        for k in ["description", "summary"]:
            if k in item:
              item[k] = fix_spacing(item[k])
    args.output.write_text(json.dumps(data, indent=2))

    (DATA_DIR / "resume.github.json").write_text(json.dumps({
        "description": "Automatic update","files":{"resume.json":{"content":args.output.read_text()}}
    }))


if __name__ == "__main__":
    main()
