PY=python
PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

.PHONY: watch publish serve devserver stopserver

html: scss content/**
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || find $(OUTPUTDIR) -mindepth 1 -delete

serve:
	cd $(OUTPUTDIR) && $(PY) -m pelican.server

scss: $(INPUTDIR)/css/style.scss 
	sassc -m --style=compressed $(INPUTDIR)/css/style.scss $(INPUTDIR)/css/style.css

publish: scss
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

deploy: publish
	ghp-import $(OUTPUTDIR) -b master
	git push origin master:master

devserver:
	$(BASEDIR)/develop_server.sh restart

stopserver:
	-kill -9 `cat pelican.pid`
	-kill -9 `cat srv.pid`
	-./develop_server.sh stop
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'
