#!/bin/bash

# Execute a notebook on the command line. Modifies the notebook inplace so the
# final execution order will be linear (from top to bottom). Running notebooks
# like this helps ensure that the final results are not a product of a
# non-linear execution order that can't be reproduced.
#
# The notebook file should be the first command line argument to this script.

# To make sure the script is stopped if any command results in an error
set -e

NOTEBOOK=$1
# nbconvert saves the executed notebook as NOTEBOOK.nbconvert.ipynb
NOTEBOOK_BACK="${NOTEBOOK/%.ipynb/.nbconvert.ipynb}"

jupyter nbconvert --to notebook --execute $NOTEBOOK
# Is the execution when well (no errors), save the executed notebook
mv $NOTEBOOK_BACK $NOTEBOOK
