# ACL Paper Submission Package

This directory contains the ACL-formatted version of the paper "Evaluating the Robustness of LLM-Based Agent Systems to Execution Environment Attacks" for submission to ACL Rolling Review.

## Directory Structure

```
acl_submission/
├── paper.tex                    # Main paper source (ACL format)
├── references.bib               # Bibliography
├── acl.sty                      # ACL style file
├── acl_natbib.bst              # ACL bibliography style
├── acl_latex.tex               # ACL template example (reference)
├── Makefile                     # Automatic compilation
├── submission_form.md           # ACL submission form checklist
├── README.md                    # This file
└── [generated files]            # .pdf, .aux, .log, etc.
```

## Quick Start

### Compile the Paper

```bash
# Basic compilation
make

# Or manually
pdflatex paper
bibtex paper
pdflatex paper
pdflatex paper
```

### Clean Build Files

```bash
# Remove auxiliary files (.aux, .log, etc.)
make clean

# Remove all generated files including PDF
make cleanall
```

### Watch Mode (Auto-compile on Changes)

```bash
# Requires 'entr' or 'inotifywait'
make watch

# Install entr on macOS:
brew install entr

# Install on Linux:
apt-get install inotify-tools  # or
dnf install entr
```

## Paper Format

The paper is formatted according to **ACL Rolling Review** requirements:

- **Document class**: `\documentclass[11pt]{article}`
- **ACL package**: `\usepackage[review]{acl}` (change to `final` for camera-ready)
- **Page limits**:
  - Short papers: 4 pages + unlimited references
  - Long papers: 8 pages + unlimited references
- **Font**: Times New Roman (11pt)
- **Margins**: ACL standard (set by acl.sty)

### Switching Between Review and Final Versions

In `paper.tex`, line 5:

```latex
% For review (anonymous)
\usepackage[review]{acl}

% For camera-ready (with author names)
\usepackage[final]{acl}

% For preprint (with page numbers, non-anonymous)
\usepackage[preprint]{acl}
```

## Submission Workflow

### 1. Prepare the Paper

- [x] Write/update content in `paper.tex`
- [x] Add references to `references.bib`
- [x] Include figures in a `figs/` subdirectory (if needed)
- [ ] Ensure paper is properly anonymized for review
- [ ] Verify all tables are generated and included

### 2. Compile and Check

```bash
make cleanall  # Start fresh
make          # Compile
open paper.pdf # Review the output
```

### 3. Update Submission Form

Edit `submission_form.md` and fill in:
- Author information
- Abstract and TL;DR
- Research area selection
- Supplementary materials info
- Consent checkboxes
- Responsible NLP checklist

### 4. Prepare Supplementary Materials

If providing code/data:

```bash
# Create software archive
tar -czf software.tgz ../../../src/ scripts/

# Create data archive
tar -czf data.tgz results/ datasets/
```

### 5. Submit to ARR

1. Go to https://openreview.net/group?id=aclweb.org/ACL/ARR
2. Create a new submission
3. Upload `paper.pdf`
4. Fill in the form fields (reference `submission_form.md`)
5. Upload supplementary materials (optional)
6. Review and submit

## Important Notes

### Anonymous Submission

For review submission, ensure:
- Author names are commented out or set to "Anonymous Submission"
- No self-identifying information in the text
- References to your own work are in third person
- No URLs that reveal identity
- Acknowledgements section is empty or removed

### Citation Format

The paper uses `acl_natbib.bst` bibliography style:

```latex
% In-text citations
\cite{author2023}           % (Author, 2023)
\citep{author2023}          % (Author, 2023)
\citet{author2023}          % Author (2023)
\citep{author2023,other2024} % (Author, 2023; Other, 2024)
```

### Table Files

The following table files are automatically copied from the parent directory:
- `model_domain_table.tex`
- `significance_table.tex`
- `temperature_significance_table.tex`

If these are missing, run:
```bash
make copy-tables
```

### Figures

To include figures from the parent directory:

```latex
% Option 1: Symbolic link
ln -s ../figs figs

% Option 2: Copy figures
cp -r ../figs/ ./figs/

% Option 3: Use relative paths in LaTeX
\includegraphics[width=0.9\textwidth]{../figs/attack_flow.pdf}
```

## Troubleshooting

### LaTeX Compilation Errors

**Issue**: Missing references or citations
```
LaTeX Warning: Citation 'xxx' on page N undefined
```
**Solution**: Run the full compilation cycle (pdflatex → bibtex → pdflatex × 2)
```bash
make cleanall && make
```

**Issue**: Missing figures
```
LaTeX Error: File 'figs/xxx.pdf' not found
```
**Solution**: Create symlink or copy figures directory
```bash
ln -s ../figs figs
```

**Issue**: Table files not found
```
LaTeX Error: File 'model_domain_table.tex' not found
```
**Solution**: Copy tables from parent directory
```bash
make copy-tables
```

### Makefile Issues

**Issue**: `make` command not found
**Solution**: Install make (usually pre-installed on macOS/Linux)
```bash
# macOS
xcode-select --install

# Ubuntu/Debian
sudo apt-get install build-essential
```

**Issue**: Watch mode not working
**Solution**: Install `entr` or `inotifywait`
```bash
# macOS
brew install entr

# Ubuntu/Debian
sudo apt-get install inotify-tools
```

## Resources

### Official ACL Resources
- **ACL Rolling Review**: https://aclrollingreview.org/
- **Style files**: https://github.com/acl-org/acl-style-files
- **Formatting guidelines**: https://acl-org.github.io/ACLPUB/formatting.html
- **Submission portal**: https://openreview.net/group?id=aclweb.org/ACL/ARR

### LaTeX Help
- **Overleaf ACL template**: https://www.overleaf.com/latex/templates/acl-conference/jvxskxpnznfj
- **ACL FAQ**: https://aclrollingreview.org/faq

## Contact

For questions about:
- **Paper content**: Contact the corresponding author (see `submission_form.md`)
- **Technical issues**: Check ACL Rolling Review FAQ
- **Submission process**: Email arr-editors@aclrollingreview.org

---

**Last updated**: 2026-02-23
