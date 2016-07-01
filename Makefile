GIT_HASH=${shell git rev-parse --verify HEAD | xargs -I [] git tag --points-at []}

ifeq "${GIT_HASH}" ""
GIT_HASH=${shell git rev-parse --verify HEAD | grep --regex '^.\{7\}' -o }
endif

VERSION=${GIT_HASH}

PROJECT_NAME=trollcat
PROJECT_TAG=trollcat

PYTHON_MODULES=trollcat

CELERY_LOG_LEVEL=INFO

WGET = wget -q

OK=\033[32m[OK]\033[39m
FAIL=\033[31m[FAIL]\033[39m
CHECK=@if [ $$? -eq 0 ]; then echo "${OK}"; else echo "${FAIL}" ; fi

default: python.mk
	@$(MAKE) -C . test

ifeq "true" "${shell test -f python.mk && echo true}"
include python.mk
endif

ifeq "true" "${shell test -f secret.mk && echo true}"
include secret.mk
endif


python.mk:
	@${WGET} https://raw.githubusercontent.com/gutomaia/makery/master/python.mk && \
		touch $@

clean: python_clean

purge: python_purge
	@rm python.mk

build: python_build

test: python_build ${REQUIREMENTS_TEST}
	${VIRTUALENV} nosetests --processes=2

dist/.check:
	@mkdir -p dist && touch $@


dist: python_wheel

distribute: dist
	scp dist/asok-0.0.1-py2-none-any.whl  gmaia@54.207.56.28:.

ci:
	${VIRTUALENV} CI=1 nosetests

pep8: ${REQUIREMENTS_TEST}
	${VIRTUALENV} pep8 --statistics -qq ${PYTHON_MODULES} | sort -rn || echo ''

todo:
	${VIRTUALENV} pep8 --first ${PYTHON_MODULES}
	find pynes -type f | xargs -I [] grep -H TODO []

search:
	find ${PYTHON_MODULES} -regex .*\.py$ | xargs -I [] egrep -H -n 'print|ipdb' [] || echo ''

report:
	coverage run --source=${PYTHON_MODULES} setup.py test

tdd:
	${VIRTUALENV} tdaemon --ignore-dirs="build,dist,bin,site,${PYTHON_MODULES}.egg-info,venv" --custom-args="--with-notify --no-start-message"


.PHONY: clean run report
