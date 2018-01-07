PY=python
PELICAN=/Users/steve/env/steveasleep/bin/pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

.PHONY: watch publish serve devserver stopserver

html: scss compile-coffee content/**
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

watch:
	make html
	fswatch -o content/**/*.md content/**/*.scss content/**/*.coffee theme/templates/*.html | xargs -n1 make html

clean:
	[ ! -d $(OUTPUTDIR) ] || find $(OUTPUTDIR) -mindepth 1 -delete

serve:
	cd $(OUTPUTDIR) && $(PY) -m pelican.server

scss: $(INPUTDIR)/css/style.scss 
	sassc $(INPUTDIR)/css/style.scss $(INPUTDIR)/css/style.css

watch-coffee:
	coffee -o $(INPUTDIR)/js --watch --compile $(INPUTDIR)/coffee/main.coffee

compile-coffee: $(INPUTDIR)/coffee/main.coffee
	coffee -o $(INPUTDIR)/js --compile $(INPUTDIR)/coffee/main.coffee

publish: scss compile-coffee
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
