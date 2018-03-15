# Source code for producing the results and figures

The code is divided between Python modules in `mypackage` and Jupyter notebooks
in `notebooks`. The modules implement the methodology and code that is reused
in different applications. This code is tested using `pytest` with the test
code in `tests`. The notebooks perform the data analysis and processing and
generate the figures for the paper.

The `Makefile` automates all processes related to executing code.
Run the following to perform all actions from building the software to
generating the final figures:

    make all


## Python package

*Describe the package here: what it does, what functions it has, etc*.


## Building, testing, and linting

Use the `Makefile` to build, test, and lint the software:

* Build and install:

        make build

* Run the static checks using flake8 and pylint:

        make check

* Run the tests in `tests` and doctests in docstrings:

        make test

* Calculate the test coverage of the main Python code (not including the
  notebooks):

        make coverage


## Generating results and figures

The Jupyter notebooks produce most of the results and figures. The `Makefile`
can execute the notebooks to generate these outputs. This is better than
executing the notebooks by hand because it ensures that cells are run
sequentially in a way that can be reproduced.

* Generate all results files specified in the `Makefile`:

        make results

* Create all figure files specified in the `Makefile`:

        make figures


## Notebooks

* [estimate-hawaii-trend.ipynb](http://nbviewer.jupyter.org/github/pinga-lab/paper-template/blob/master/code/notebooks/estimate-hawaii-trend.ipynb):
  Calculate a linear trend for the temperature data of Hawaii.
* [figure-hawaii-trend.ipynb](http://nbviewer.jupyter.org/github/pinga-lab/paper-template/blob/master/code/notebooks/figure-hawaii-trend.ipynb):
  Make a figure of the estimated trend for the paper.
