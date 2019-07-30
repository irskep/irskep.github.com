# .PHONY: resume.html

all: resume.html resume2.html resume3.html

resume.html: theme1.css template.html json2html.py resume.json
	pipenv run ./json2html.py 3 1 resume.json theme1.css resume.html

resume2.html: theme2.css template.html json2html.py resume.json
	pipenv run ./json2html.py 3 2 resume.json theme2.css resume2.html

resume3.html: theme3.css template.html json2html.py resume.json
	pipenv run ./json2html.py 3 3 resume.json theme3.css resume3.html

resume.json: OPS epub2json.py
	pipenv run ./epub2json.py OPS/chapter-1.xhtml resume.json

OPS: original.epub
	unzip -o original.epub
