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
	cat less/literally.css less/colorpicker.css > assets/css/lc.css

img:
	mkdir -p assets/img
	cp -r img/* assets/img/

bootstrap_js:
	mkdir -p assets/js
	cp js/jquery-1.7.2.min.js assets/js/jquery-1.7.2.min.js

js:
	coffee --compile -o assets/js coffee/*

watch:
	echo "Watching less files..."; \
	watchr -e "watch('less/.*\.less') { system 'make' }"


.PHONY: watch css img js
