.PHONY: resume.html

all: resume.html

resume.html: chapter-1.xhtml convert.py
	pipenv run ./convert.py OPS/chapter-1.xhtml resume.html

chapter-1.xhtml: original.epub
	unzip -o original.epub
