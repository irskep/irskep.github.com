#!/usr/bin/env sh

set -e
poetry run python yaml2html.py -f resume.yaml -o resume.html
typst compile resume.typ ../content/downloads/Steve_Landey_resume.pdf
