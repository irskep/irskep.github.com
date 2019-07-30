# .PHONY: resume.html

all: resume.html

resume.html: theme1.css template.html json2html.py resume.json
	pipenv run ./json2html.py resume.json theme1.css resume.html

resume.json: OPS epub2json.py
	pipenv run ./epub2json.py OPS/chapter-1.xhtml resume.json

OPS: original.epub
	unzip -o original.epub
