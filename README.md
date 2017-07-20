# Paper template for open science projects

A [cookiecutter](https://github.com/audreyr/cookiecutter) template for an open
science paper.

Generates the basic layout of a repository including data, code, results, and
the paper manuscript.

Has a few assumptions about technology choices:

* Use the conda package manager
* Write documents in Latex.
* Produce results in Jupyter notebooks
* Run tests using pytest

Also assumes that you're OK with using the BSD 3-clause license for code and
CC-BY for data.


## Using

1. Create an empty repository on Github (or anywhere else you want). Don't make
   any commits or clone the repository yet.
2. Install cookiecuter: `conda install -c conda-forge cookiecutter`
3. Download the `cookiecuter.json` configuration file from this repository to
   the current directory
4. Edit the file to reflect your project
5. Generate your project folder from the template by running
   `cookiecutter gh:pinga-lab/paper-template --no-input` (we'll refer to it as
   `sample-paper`)
6. Enter the folder and start a git repository:

        cd sample-paper
        git init

7. Add your Github repository as a remote, commit the new files, and push to
   Github:

        git remote add origin GITHUB_CLONE_URL
        git add .
        git commit
        git push


## Contributing

Pull Requests are more than welcome!


## License

All source code is made available under a BSD 3-clause license.  You can freely
use and modify the code, without warranty, so long as you provide attribution
to the authors.  See `LICENSE.md` for the full license text.
