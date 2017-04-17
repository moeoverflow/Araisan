#
# See ./CONTRIBUTING.rst
#

VERSION=$(shell grep __version__ araisan/__init__.py)
REQUIREMENTS="requirements-dev.txt"
TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"


all: test


init: uninstall-araisan
	@echo $(TAG)Installing dev requirements$(END)
	pip install --upgrade -r $(REQUIREMENTS)

	@echo $(TAG)Installing Araisan$(END)
	pip install --upgrade --editable .

	@echo


test: init
	@echo $(TAG)Running tests on the current Python interpreter with coverage $(END)
	py.test --cov ./araisan --cov ./tests --doctest-modules --verbose ./araisan ./tests
	@echo

test-dist: test-sdist test-bdist-wheel
	@echo


test-sdist: clean uninstall-araisan
	@echo $(TAG)Testing sdist build an installation$(END)
	python setup.py sdist
	pip install --force-reinstall --upgrade dist/*.gz
	@echo


test-bdist-wheel: clean uninstall-araisan
	@echo $(TAG)Testing wheel build an installation$(END)
	python setup.py bdist_wheel
	pip install --force-reinstall --upgrade dist/*.whl
	@echo


# This tests everything, even this Makefile.
test-all: uninstall-all clean init test test-dist


publish: test-all publish-no-test

publish-no-test:
	@echo $(TAG)Testing wheel build an installation$(END)
	@echo "$(VERSION)"
	@echo "$(VERSION)" | grep -q "dev" && echo '!!!Not publishing dev version!!!' && exit 1 || echo ok
	python setup.py register
	python setup.py sdist upload
	python setup.py bdist_wheel upload
	@echo


clean:
	@echo $(TAG)Cleaning up$(END)
	rm -rf *.egg dist build .coverage
	find . -name '__pycache__' -delete -print -o -name '*.pyc' -delete -print
	@echo


uninstall-araisan:
	@echo $(TAG)Uninstalling araisan$(END)
	- pip uninstall --yes araisan &2>/dev/null

	@echo "Verifying…"
	cd .. && ! python -m araisan --version &2>/dev/null

	@echo "Done"
	@echo


uninstall-all: uninstall-araisan

	@echo $(TAG)Uninstalling araisan requirements$(END)
	- pip uninstall --yes pyyaml

	@echo $(TAG)Uninstalling development requirements$(END)
	- pip uninstall --yes -r $(REQUIREMENTS)
