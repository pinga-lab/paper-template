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

# Execute a notebook on the command line. Modifies the notebook inplace so the
# final execution order will be linear (from top to bottom). Running notebooks
# like this helps ensure that the final results are not a product of a
# non-linear execution order that can't be reproduced.
RUN = bash run_notebook.sh


# TARGETS
###############################################################################

help:
	@echo "Commands:"
	@echo ""
	@echo "  all        runs 'build', 'test', and 'figures'"
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


# Clean does not remove results or figure files to avoid accidentally deleting
# the results of long running computations.
clean:
	find . -name "*.pyc" -exec rm -v {} \;
	rm -rvf build dist MANIFEST *.egg-info __pycache__ .coverage .cache


# Run all steps to generate the final figures. Results files are generated
# based on the figure requirements (see below).
all: build test figures


# Generating results
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Main target for producing all results. Add results files as dependencies to
# include them in the build.
results: $(RESDIR)/hawaii-trend.csv


# Build a result file from a notebook and a data file.
# Execution modifies a notebook, so the time stamp will be later than the
# target. touch the target to make sure it's always newer than the dependency.
$(RESDIR)/hawaii-trend.csv: $(NBDIR)/estimate-hawaii-trend.ipynb $(DATADIR)/hawaii-TAVG-Trend.txt
	$(RUN) $<
	@touch $@



# Generating figures
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Main target for generating figures. Include figure files as dependencies to
# include them in the build.
figures: $(FIGDIR)/hawaii-trend.eps


# Generate a figure file from a notebook and a results file.
$(FIGDIR)/hawaii-trend.eps: $(NBDIR)/figure-hawaii-trend.ipynb $(RESDIR)/hawaii-trend.csv
	$(RUN) $<
	@touch $@



# Building and testing the code
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

build:
	pip install --no-deps -e .

test:
	pytest $(PYTEST_ARGS) $(PACKAGE) $(TESTDIR)

coverage:
	pytest $(PYTEST_COV_ARGS) --cov=$(PACKAGE) $(PYTEST_ARGS) $(PACKAGE) $(TESTDIR)

check: pep8 lint

pep8:
	flake8 $(PACKAGE) $(TESTDIR) setup.py

lint:
	pylint $(PACKAGE) setup.py
