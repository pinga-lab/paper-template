# Paper title

by
Author 1,
Author 2,
etc

This paper has been submitted for publication in *Some Journal*.

Brief description of what this paper is about (2-3 sentences). Include a figure
as well with the main result of your paper.

![Figure goes here.](https://raw.githubusercontent.com/pinga-lab/PAPER-REPO/master/FIGURE_FILE)
Brief figure caption.


## Abstract

Paste here the abstract.


## Reproducing the results

You can download a copy of all the files in this repository by cloning the
[git](https://git-scm.com/) repository:

    git clone https://github.com/pinga-lab/PAPER-REPO.git

or [click here to download a zip archive](https://github.com/pinga-lab/PAPER-REPO/archive/master.zip).

*Describe here the folder structure and what is in each folder. Suggested
layout would be:*

All source code used to generate the results and figures in the paper are in
the `code` folder.
The data used in this study is provided in `data` and the sources for the
manuscript text and figures are in `manuscript`.
See the `README.md` files in each directory for a full description.

The calculations and figure generation are all run inside
[Jupyter notebooks](http://jupyter.org/).
You can view a static (non-executable) version of the notebooks in the
[nbviewer]() webservice:

http://nbviewer.jupyter.org/github/pinga-lab/PAPER-REPO

Also provided are read-only PDF versions of the notebooks.

See sections below for instructions on executing the code.


### Setting up your environment

Describe what you need to install. Usually it's Anaconda with Python 2.7. Here
is template for that:

> You'll need a working Python **2.7** environment with all the standard
> scientific packages installed (numpy, scipy, matplotlib, etc).  The easiest
> (and recommended) way to get this is to download and install the
> [Anaconda Python distribution](http://continuum.io/downloads#all).
> Make sure you get the **Python 2.7** version.

If you need Fatiando, use this:

> You'll also need to install version X.Y of the
> [Fatiando a Terra](http://www.fatiando.org/) library.
> See the install instructions on the website.

If you provide a conda environment through an `environment.yml` file, use:

> You can use `conda` package manager (included in Anaconda) to create a
> virtual environment with all the required packages installed.
> Run the following command in the repository folder (where `environment.yml`
> is located):

    conda env create

> To activate the conda environment, run

    source activate moho

> or, if you're on Windows,

    activate moho

> This will enable the environment for your current terminal session.

I would recommend having a bash shell with `make` installed in Windows to make
life easier for everyone. Put these instructions if you want this:

> **Windows users:** It is highly recommended that you install the bash shell
> to run code and produce the results here.
> You can download bash for Windows at http://git-for-windows.github.io/.
> Install the "Git for Windows SDK" that will come with bash and `make` as
> well.


### Running the code

If using Jupyter notebooks, use this text:

> To execute the code in the Jupyter notebooks, you must first start the
> notebook server by going into the repository folder and running:

    jupyter notebook

> Make sure you have the `conda` environment enabled first.

> This will start the server and open your default web browser to the Jupyter
> interface. In the page, go into the `code` folder and select the
> notebook that you wish to view/run.

> The notebook is divided cells (some have text while other have code).
> Each cell can be executed using `Shift + Enter`.
> Executing text cells does nothing and executing code cells runs the code
> and produces it's output.
> To execute the whole notebook, run all cells in order.


## License

All source code is made available under a BSD 3-clause license.  You can freely
use and modify the code, without warranty, so long as you provide attribution
to the authors.  See `LICENSE.md` for the full license text.

The manuscript text is not open source. The authors reserve the rights to the
article content, which is currently submitted for publication in the
JOURNAL NAME.
