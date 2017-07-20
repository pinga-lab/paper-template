# Latex source files for the manuscript

The `Makefile` has rules for building the PDF of the manuscript. To build the
PDF, run:

    make

To estimate the number of words in the paper (useful for estimating number of
pages):

    make wc


## Generating a PDF with marked changes

One of the biggest advantages of using version control is that we are able to
revert and compare any changes made to the manuscript.
Follow these instructions to generate a PDF with marked changes between the
current version and a previous commit (marked by a git tag).

1. Tag the commit with the original version. It's useful to tag the commit with
   the version submitted to the journal. Use `git tag submission` to add the
   tag. Remember to run `git push --tags` to make sure the tags are synced to
   Github. If you used a different tag, change `R1_GIT_TAG` in `Makefile`.
2. Enable the new command `git ldiff` by adding the following lines to the
   `.gitconfig` file in your home directory:

        [difftool.latex]
            cmd = latexdiff "$LOCAL" "$REMOTE"
        [alias]
            ldiff = difftool -y -t latex

3. Run `make r1` and rejoice.
