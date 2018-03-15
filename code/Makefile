# Manages building, testing, and cleaning the code as well as running the code
# to generate the results and figures for the paper.

# CONFIGURATION
###############################################################################

# Set the package name
PACKAGE = mypackage

TESTDIR = tests
RESDIR = ../results
DATADIR = ../data
FIGDIR = ../manuscript/figures
NBDIR = notebooks

PYTEST_ARGS = --doctest-modules -v
PYTEST_COV_ARGS = --cov-report=term-missing

# Execute a notebook on the command line. Doesn't overwrites the content of the
# notebook.
RUN = bash run_notebook.sh

# TARGETS
###############################################################################

help:
	@echo "Commands:"
	@echo ""
	@echo "  build      build and install the package"
	@echo "  test       run the test suite (including doctests)"
	@echo "  coverage   calculate test coverage"
	@echo "  check      run all code quality checks (pep8, linter)"
	@echo "  pep8       check for PEP8 style compliance"
	@echo "  lint       run static analysis using pylint"
	@echo "  clean      clean up the package build"
	@echo "  results    execute all of the results generating notebooks"
	@echo "  figures    execute all of the figure generating notebooks"
	@echo ""

all: check build test results figures


# Generating results
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

results: $(RESDIR)/hawaii-trend.csv

$(RESDIR)/hawaii-trend.csv: $(NBDIR)/estimate-hawaii-trend.ipynb $(DATADIR)/hawaii-TAVG-Trend.txt
	$(RUN) $<



# Generating figures
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

figures: $(FIGDIR)/hawaii-trend.eps

$(FIGDIR)/hawaii-trend.eps: $(NBDIR)/figure-hawaii-trend.ipynb $(RESDIR)/hawaii-trend.csv
	$(RUN) $<



# Building and testing the code
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

build:
	pip install --no-deps -e .

test:
	pytest $(PYTEST_ARGS) $(PACKAGE) $(TESTDIR)

coverage:
	# Run a tmp folder to make sure the tests are run on the installed version
	pytest $(PYTEST_COV_ARGS) --cov=$(PACKAGE) $(PYTEST_ARGS) $(PACKAGE) $(TESTDIR)

check: pep8 lint

pep8:
	flake8 $(PACKAGE) $(TESTDIR) setup.py

lint:
	pylint $(PACKAGE) setup.py

clean:
	find . -name "*.pyc" -exec rm -v {} \;
	rm -rvf build dist MANIFEST *.egg-info __pycache__ .coverage .cache
