#!/bin/bash
set -e

NOTEBOOK=$1
NOTEBOOK_BACK="${NOTEBOOK/%.ipynb/.nbconvert.ipynb}"

jupyter nbconvert --to notebook --execute $NOTEBOOK
mv $NOTEBOOK_BACK $NOTEBOOK
