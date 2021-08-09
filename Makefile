HOST_PYTHON := python3.9
PYTHON := ./venv/bin/python

all: venv

venv: | requirements.in
	$(HOST_PYTHON) -m venv venv
	$(PYTHON) -m pip install pip-tools
	test -f requirements.txt || $(PYTHON) -m piptools compile \
		requirements.in \
		--no-header \
		--quiet \
		-o requirements.txt
	$(PYTHON) -m pip install -r requirements.txt
	$(PYTHON) -m pip install black isort pylint

clean:
	rm -Rf venv

#
# TESTING
#
.python-files:
	find ./frontenis -type f -name "*.py" -print > $@

.INTERMEDIATE: .python-files

with_python_files := xargs --arg-file .python-files

check: check-black check-isort check-pylint

check-black: venv | .python-files
	$(with_python_files) $(PYTHON) -m black \
		--line-length 80 \
		--target-version py39 \
		--check \
		--diff

check-isort: venv | .python-files
	$(with_python_files) $(PYTHON) -m isort \
		--check-only \
		--diff

check-pylint: venv | .python-files
	$(with_python_files) $(PYTHON) -m pylint

.PHONY: check clean
