NOTEBOOKS := $(wildcard *.ipynb)
NOTEBOOK_PDFS := $(NOTEBOOKS:.ipynb=.pdf)


# Convert the Jupyter notebooks to PDF for offline reading
pdfs: $(NOTEBOOK_PDFS)

%.pdf: %.ipynb
	jupyter nbconvert --to pdf $<

# Run tests in the "tests" directory
test:
	pytest --doctest-modules -v tests

# Static checks for format and common errors
check: pep8

pep8:
	flake8 *.py tests

clean:
	rm -rf $(NOTEBOOK_PDFS)
	find . -name "*.pyc" -exec rm -v {} \;
