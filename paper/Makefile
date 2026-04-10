## Makefile for compiling the Copernicus GMD manuscript
##
## Usage:
##   make        – compile the PDF (default target)
##   make clean  – remove auxiliary files
##   make purge  – remove all generated files including the PDF
##
## Prerequisites:
##   - A working LaTeX distribution (TeX Live ≥ 2020 or MiKTeX ≥ 21)
##   - The Copernicus LaTeX template files (copernicus.cls, copernicus.bst)
##     downloaded from https://publications.copernicus.org/for_authors/manuscript_preparation.html
##     and placed in this directory.

PAPER   = ms
LATEXMK = latexmk
LATEX   = pdflatex
BIBTEX  = bibtex

.PHONY: all clean purge

## Default target: compile PDF
all: $(PAPER).pdf

## Build with latexmk if available, otherwise fall back to manual multi-pass
$(PAPER).pdf: $(PAPER).tex references.bib
	@if command -v $(LATEXMK) > /dev/null 2>&1; then \
	    $(LATEXMK) -pdf -interaction=nonstopmode $(PAPER).tex; \
	else \
	    $(LATEX) -interaction=nonstopmode $(PAPER).tex; \
	    $(BIBTEX) $(PAPER); \
	    $(LATEX) -interaction=nonstopmode $(PAPER).tex; \
	    $(LATEX) -interaction=nonstopmode $(PAPER).tex; \
	fi

## Remove auxiliary files but keep the PDF
clean:
	@$(LATEXMK) -c 2>/dev/null || true
	@rm -f $(PAPER).aux $(PAPER).bbl $(PAPER).blg \
	       $(PAPER).log $(PAPER).out $(PAPER).toc \
	       $(PAPER).lof $(PAPER).lot $(PAPER).fls \
	       $(PAPER).fdb_latexmk $(PAPER).synctex.gz \
	       $(PAPER).run.xml

## Remove all generated files including the PDF
purge: clean
	@rm -f $(PAPER).pdf
