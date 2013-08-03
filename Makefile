PY=python
PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

FTP_HOST=localhost
FTP_USER=anonymous
FTP_TARGET_DIR=/

SSH_HOST=localhost
SSH_PORT=22
SSH_USER=root
SSH_TARGET_DIR=/var/www

S3_BUCKET=my_s3_bucket

DROPBOX_DIR=~/Dropbox/Public/

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   make publish                     generate using production settings '
	@echo '   make serve                       serve site at http://localhost:8000'
	@echo '   make devserver                   start/restart develop_server.sh    '
	@echo '   make stopserver                  stop local server                  '
	@echo '   deploy-beta                      upload to /beta via gh-pages'
	@echo '   deploy-prod                      upload to /via gh-pages'
	@echo '                                                                       '


html: clean compile-scss compile-coffee $(OUTPUTDIR)/index.html

$(OUTPUTDIR)/%.html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || find $(OUTPUTDIR) -mindepth 1 -delete

regenerate: clean
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
	cd $(OUTPUTDIR) && $(PY) -m pelican.server

devserver:
	$(BASEDIR)/develop_server.sh restart

stopserver:
	-kill -9 `cat pelican.pid`
	-kill -9 `cat srv.pid`
	-./devserver.sh stop
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

watch-scss:
	sass --watch $(INPUTDIR)/css/style.scss:$(INPUTDIR)/css/style.css

compile-scss:
	sass --update $(INPUTDIR)/css/style.scss:$(INPUTDIR)/css/style.css

watch-coffee:
	coffee -o $(INPUTDIR)/js --watch --compile $(INPUTDIR)/coffee/main.coffee

compile-coffee:
	coffee -o $(INPUTDIR)/js --compile $(INPUTDIR)/coffee/main.coffee

publish: compile-scss compile-coffee
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

deploy-beta: publish
	ghp-import $(OUTPUTDIR)
	git push beta gh-pages

deploy-prod: publish
	ghp-import $(OUTPUTDIR)
	git push origin gh-pages

.PHONY: html help clean regenerate serve devserver publish deploy-beta deploy-prod
