# Makefile for the paper

# sources
BASE = resex

SOURCES = $(BASE).tex bibliography.bib Makefile \
  $(wildcard *.png) $(wildcard CHG1b*.pdf)

# tools
TEX = pdflatex
BIB = bibtex

.PHONY: all refresh clean

all: $(BASE).pdf

# generate PDF
$(BASE).pdf: $(SOURCES)
	$(TEX) $(BASE); $(BIB) $(BASE); $(TEX) $(BASE); $(TEX) $(BASE)

# refresh
refresh:
	touch $(BASE).tex

# cleanup
clean:
	rm -f $(BASE).aux
	rm -f $(BASE).bbl
	rm -f $(BASE)Notes.bib
	rm -f $(BASE).blg
	rm -f $(BASE).log
