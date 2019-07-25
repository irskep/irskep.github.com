# .PHONY: resume.html

all: resume.html

resume.html: theme1.css OPS convert.py template.html
	pipenv run ./convert.py OPS/chapter-1.xhtml theme1.css resume.html

OPS: original.epub
	unzip -o original.epub
