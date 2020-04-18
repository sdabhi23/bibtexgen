# BibtexGen

A simple cli tool to generate a list of references of any paper available on Semantic Scholar as a .bib file.

## Installation

This package supports only Python 3.5 and above.

```bash
$ pip install bibtexgen
    Installing build dependencies ... done
    Getting requirements to build wheel ... done
        Preparing wheel metadata ... done
.
.
.
Successfully built bibtexgen
Installing collected packages: bibtexgen
Successfully installed bibtexgen-0.0.1
```

## Usage

```bash
$ bibtexgen


================================= Welcome to BibTex Generator =================================


Please enter the Sematic Scholar Id of your paper: 6258b37b8d517f121c844ebad226da472761adc6

Creating file 6258b37b8d517f121c844ebad226da472761adc6_references.bib

100%|████████████████████████████████████████████████████████████████████████████████████| 8/8 [00:21<00:00,  2.63s/papers]

Your references have been saved!
```