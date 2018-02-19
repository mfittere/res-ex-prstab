# Makefile for the paper

# sources
BASE = resex

SOURCES = $(BASE).tex resex-bibdesk.bib Makefile \
  $(wildcard *.png) $(wildcard CHG1b*.pdf) diffusion_illustration.pdf

# tools
TEX = pdflatex
BIB = bibtex

.PHONY: all clean

all: $(BASE).pdf

# generate PDF
$(BASE).pdf: $(SOURCES)
	$(TEX) $(BASE); $(BIB) $(BASE); $(TEX) $(BASE); $(TEX) $(BASE)

# cleanup
clean:
	rm -f $(BASE).aux
	rm -f $(BASE).bbl
	rm -f $(BASE)Notes.bib
	rm -f $(BASE).blg
	rm -f $(BASE).log
	rm -f $(BASE).out
