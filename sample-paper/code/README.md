# Source code for producing the results and figures

Describe your code briefly here.

List of notebooks:

* [generate_figures.ipynb](http://nbviewer.jupyter.org/github/pinga-lab/sample-paper/blob/master/code/generate_figures.ipynb):
  Make all the results figures in the paper.

The `Makefile` has the following rules:

* `make test`: run unit and integration tests
* `make check`: run static checks on the code
* `make pdfs`: convert all notebooks to PDF
* `make clean`: remove generated files
