# GMD Manuscript

This directory contains the LaTeX source for the Geoscientific Model
Development (GMD) paper describing the `icon_validation` software.

## Directory structure

```
paper/
├── ms.tex           Main manuscript (LaTeX)
├── references.bib   Bibliography
├── Makefile         Build script
└── figures/         Figures referenced in the manuscript
    └── README.txt   Notes on expected figure files
```

## Prerequisites

Before compiling, download the official Copernicus LaTeX template files from
<https://publications.copernicus.org/for_authors/manuscript_preparation.html>
and place the following files in this directory:

- `copernicus.cls` — LaTeX document class
- `copernicus.bst` — BibTeX bibliography style

## Compilation

```bash
make        # compile PDF (uses latexmk if available)
make clean  # remove auxiliary files
make purge  # remove all generated files including PDF
```

A standard four-pass manual compilation also works:

```bash
pdflatex ms.tex
bibtex   ms
pdflatex ms.tex
pdflatex ms.tex
```

## Completing the template

Placeholder text in the manuscript is enclosed in square brackets, e.g.
`[Author 1]`, `[Institution 1, City, Country]`, `[ZENODO_DOI]`.
Replace all placeholders with the appropriate information before submission.
