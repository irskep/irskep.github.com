#!/usr/bin/env sh

set -e
poetry run python yaml2outputs.py
typst compile resume.typst ../content/downloads/Steve_Landey_resume.pdf
