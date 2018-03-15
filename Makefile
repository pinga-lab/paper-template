# Build the software, test it, generate the results and plots, and compile the
# manuscript PDF.
#
# Runs the individual Makefiles from code/ and manuscript/.

all:
	make -C code all
	make -C manuscript all
