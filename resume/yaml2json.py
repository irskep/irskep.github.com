import argparse
import json
import os
import pathlib
import yaml

DATA_DIR = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("-f", "--file", type=pathlib.Path)
    p.add_argument("-o", "--output", type=pathlib.Path)

    args = p.parse_args()

    args.output.write_text(json.dumps(yaml.safe_load(args.file.read_text()), indent=2))


if __name__ == "__main__":
    main()
