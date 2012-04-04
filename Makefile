BOOTSTRAP = ./css/bootstrap.css
BOOTSTRAP_LESS = ./less/bootstrap.less
STYLE = ./less/style.less
BOOTSTRAP_RESPONSIVE = ./css/bootstrap-responsive.css
BOOTSTRAP_RESPONSIVE_LESS = ./less/responsive.less
LESS_COMPRESSOR ?= `which lessc`
WATCHR ?= `which watchr`

all: css img js bootstrap_js

css:
	mkdir -p assets/css
	lessc ${BOOTSTRAP_LESS} > assets/css/bootstrap.css
	lessc --compress ${BOOTSTRAP_LESS} > assets/css/bootstrap.min.css
	lessc ${BOOTSTRAP_RESPONSIVE_LESS} > assets/css/bootstrap-responsive.css
	lessc --compress ${BOOTSTRAP_RESPONSIVE_LESS} > assets/css/bootstrap-responsive.min.css
	lessc ${STYLE} > assets/css/style.css
	lessc --compress ${STYLE} > assets/css/style.min.css

img:
	mkdir -p assets/img
	cp img/* assets/img/

bootstrap_js:
	mkdir -p assets/js
	cp js/jquery-1.7.2.min.js assets/js/jquery-1.7.2.min.js
	cat js/bootstrap-transition.js js/bootstrap-alert.js js/bootstrap-button.js js/bootstrap-carousel.js js/bootstrap-collapse.js js/bootstrap-dropdown.js js/bootstrap-modal.js js/bootstrap-tooltip.js js/bootstrap-popover.js js/bootstrap-scrollspy.js js/bootstrap-tab.js js/bootstrap-typeahead.js > assets/js/bootstrap.js
	uglifyjs -nc assets/js/bootstrap.js > assets/js/bootstrap.min.tmp.js
	echo "/**\n* Bootstrap.js by @fat & @mdo\n* Copyright 2012 Twitter, Inc.\n* http://www.apache.org/licenses/LICENSE-2.0.txt\n*/" > assets/js/copyright.js
	cat assets/js/copyright.js assets/js/bootstrap.min.tmp.js > assets/js/bootstrap.min.js
	rm assets/js/copyright.js assets/js/bootstrap.min.tmp.js

js:
	coffee --compile -o assets/js coffee/*

watch:
	echo "Watching less files..."; \
	watchr -e "watch('less/.*\.less') { system 'make' }"


.PHONY: watch css img js
