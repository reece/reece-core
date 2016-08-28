# Makefile for Python project

.DELETE_ON_ERROR:
.PHONY: FORCE
.SUFFIXES :

SHELL:=/bin/bash -o pipefail
SELF:=$(firstword $(MAKEFILE_LIST))

############################################################################
#= BASIC USAGE
default: help

#=> help -- display this help message
help:
	@sbin/makefile-extract-documentation "${SELF}"


############################################################################
#= SETUP, INSTALLATION, PACKAGING

#=> develop: install package in develop mode
.PHONY: develop
develop: %:
	[ -f requirements.txt ] && pip install --upgrade -r requirements.txt || true
	python setup.py $*

#=> install: install package
#=> bdist bdist_egg bdist_wheel build build_sphinx install sdist
.PHONY: bdist bdist_egg bdist_wheel build build_sphinx install sdist
bdist bdist_egg bdist_wheel build build_sphinx install sdist: %:
	python setup.py $@

#=> upload: upload to pypi
#=> upload_*: upload to named pypi service (requires config in ~/.pypirc)
.PHONY: upload upload_%
upload: upload_pypi
upload_%:
	python setup.py bdist_egg bdist_wheel sdist upload -r $*

############################################################################
#= TESTING

#=> test: execute tests
.PHONY: test
test:
	py.test tests

#=> tox: execute tests via tox
.PHONY: tox
tox:
	tox


############################################################################
#= UTILITY TARGETS
# N.B. Although code is stored in github, I use hg and hg-git on the command line
#=> reformat: reformat code with yapf and commit
.PHONY: reformat
reformat:
	@if hg sum | grep -qL '^commit:.*modified'; then echo "Repository not clean" 1>&2; exit 1; fi
	@if hg sum | grep -qL ' applied'; then echo "Repository has applied patches" 1>&2; exit 1; fi
	yapf -i -r seqrepo tests
	hg commit -m "reformatted with yapf"

#=> docs -- make sphinx docs
.PHONY: doc docs
doc docs: develop
	# RTD makes json. Build here to ensure that it works.
	make -C doc html json

#=> clean: remove temporary and backup files
.PHONY: clean
clean:
	find . \( -name \*~ -o -name \*.bak \) -print0 | xargs -0r rm

#=> cleaner: remove files and directories that are easily rebuilt
.PHONY: cleaner
cleaner: clean
	rm -fr *.egg-info build dist
	find . \( -name \*.pyc -o -name \*.orig \) -print0 | xargs -0r rm
	find . -name __pycache__ -print0 | xargs -0r rm -fr

#=> cleaner: remove files and directories that require more time/network fetches to rebuild
.PHONY: cleanest distclean
cleanest distclean: cleaner
	rm -fr .eggs .tox

## <LICENSE>
## Copyright 2016 Source Code Committers
## 
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
## 
##     http://www.apache.org/licenses/LICENSE-2.0
## 
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
## </LICENSE>
