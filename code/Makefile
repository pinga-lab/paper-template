NOTEBOOKS := $(shell find . -maxdepth 1 -name '*.ipynb')
NOTEBOOK_PDFS := $(NOTEBOOKS:.ipynb=.pdf)

all: pdf

pdf: $(NOTEBOOK_PDFS)

# Convert the Jupyter notebooks to PDF for offline reading
%.pdf: %.ipynb
	jupyter nbconvert --to pdf $<

clean:
	rm -rf $(NOTEBOOK_PDFS)
	find . -name "*.pyc" -exec rm -v {} \;
