#!/usr/bin/env sh

set -e
poetry run python yaml2outputs.py
typst compile resume.typ ../content/downloads/Steve_Landey_resume.pdf
