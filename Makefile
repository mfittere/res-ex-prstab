# Makefile for the paper

# sources
BASE = resex

SOURCES = $(BASE).tex $(BASE).bib Makefile \
  $(wildcard *.png) $(wildcard CHG1b*.pdf) diffusion_illustration.pdf

# tools
TEX = pdflatex
BIB = bibtex

.PHONY: all clean

all: $(BASE).pdf response.pdf

# generate PDFs
$(BASE).pdf: $(SOURCES)
	$(TEX) $(BASE); $(BIB) $(BASE); $(TEX) $(BASE); $(TEX) $(BASE)

response.pdf: response.tex Makefile
	$(TEX) $<

# cleanup
clean:
	rm -f $(BASE).aux
	rm -f $(BASE)Notes.bib
	rm -f $(BASE).blg
	rm -f $(BASE).log
	rm -f $(BASE).out
