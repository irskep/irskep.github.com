PY=poetry run python
PELICAN=poetry run pelican -D
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

.PHONY: watch serve devserver stopserver

output: content/** resume/** timeline
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) --verbose

clean:
	[ ! -d $(OUTPUTDIR) ] || find $(OUTPUTDIR) -mindepth 1 -delete

serve:
	cd $(OUTPUTDIR) && $(PY) -m pelican.server 8001

pelican:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

resume-html:
	poetry run python -m resume.yaml2html -f resume/resume.yaml -o content/resume.html

resume-json:
	poetry run python -m resume.yaml2json -f resume/resume.yaml -o content/resume.json	

resume-pdf:
	typst compile resume/resume.typ content/downloads/Steve_Landey_resume.pdf

timeline: timeline/**
	cd timeline && yarn build && cd ..
	cp -r timeline/dist content/timeline

deploy: output
	poetry run ghp-import $(OUTPUTDIR) -b master
	git push origin master:master

devserver:
	$(PELICAN) -lr --port 8001
