#! /bin/sh

latex thesis && \
bibtex thesis && \
pdflatex thesis
# latex thesis && \
# dvipdf thesis

# with biblatex, it is only necessary to run latex once after bibtex, not twice.
# with older tex installations, you may need to change 'biber' to 'bibtex'
