PY=poetry run python
PELICAN=poetry run pelican -D
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

.PHONY: watch publish serve devserver stopserver resume

html: content/**
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) --verbose

clean:
	[ ! -d $(OUTPUTDIR) ] || find $(OUTPUTDIR) -mindepth 1 -delete

serve:
	cd $(OUTPUTDIR) && $(PY) -m pelican.server 8001

pelican:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

publish: pelican
	cd timeline && yarn build && cd ..
	cp resume/resume.html resume/resume*.html output/
	cp -r timeline/dist output/timeline

deploy: publish
	poetry run ghp-import $(OUTPUTDIR) -b master
	git push origin master:master

devserver:
	$(PELICAN) -lr --port 8001

resume:
	cd resume && make all
