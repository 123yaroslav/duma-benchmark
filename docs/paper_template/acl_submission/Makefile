# Makefile for ACL paper compilation
# Usage:
#   make          - Compile paper.pdf
#   make clean    - Remove auxiliary files
#   make cleanall - Remove all generated files including PDF
#   make watch    - Continuously compile on changes (requires entr or inotifywait)

# Main document name (without .tex extension)
MAIN = paper

# LaTeX compiler
LATEX = pdflatex
BIBTEX = bibtex

# Flags for pdflatex
LATEXFLAGS = -interaction=nonstopmode -halt-on-error

# Source files
SOURCES = $(MAIN).tex references.bib acl.sty acl_natbib.bst
TABLES = model_domain_table.tex significance_table.tex temperature_significance_table.tex

# Generated files
PDF = $(MAIN).pdf
AUX_FILES = $(MAIN).aux $(MAIN).bbl $(MAIN).blg $(MAIN).log $(MAIN).out $(MAIN).toc

.PHONY: all clean cleanall watch help copy-tables

# Default target
all: $(PDF)

# Main compilation target
$(PDF): $(SOURCES) $(TABLES)
	@echo "==> First LaTeX pass..."
	$(LATEX) $(LATEXFLAGS) $(MAIN)
	@echo "==> Running BibTeX..."
	-$(BIBTEX) $(MAIN)
	@echo "==> Second LaTeX pass..."
	$(LATEX) $(LATEXFLAGS) $(MAIN)
	@echo "==> Third LaTeX pass..."
	$(LATEX) $(LATEXFLAGS) $(MAIN)
	@echo "==> PDF generated: $(PDF)"

# Copy table files from parent directory
copy-tables:
	@echo "==> Copying table files..."
	@if [ -f ../model_domain_table.tex ]; then \
		cp ../model_domain_table.tex .; \
		echo "Copied model_domain_table.tex"; \
	else \
		echo "Warning: ../model_domain_table.tex not found"; \
	fi
	@if [ -f ../significance_table.tex ]; then \
		cp ../significance_table.tex .; \
		echo "Copied significance_table.tex"; \
	else \
		echo "Warning: ../significance_table.tex not found"; \
	fi
	@if [ -f ../temperature_significance_table.tex ]; then \
		cp ../temperature_significance_table.tex .; \
		echo "Copied temperature_significance_table.tex"; \
	else \
		echo "Warning: ../temperature_significance_table.tex not found"; \
	fi

# Clean auxiliary files
clean:
	@echo "==> Cleaning auxiliary files..."
	rm -f $(AUX_FILES)
	@echo "==> Clean complete"

# Clean all generated files including PDF
cleanall: clean
	@echo "==> Removing PDF..."
	rm -f $(PDF)
	@echo "==> Clean all complete"

# Watch for changes and recompile (requires entr or inotifywait)
watch:
	@if command -v entr > /dev/null 2>&1; then \
		echo "==> Watching for changes (using entr)..."; \
		echo "Press Ctrl+C to stop"; \
		echo $(SOURCES) $(TABLES) | tr ' ' '\n' | entr -c make $(PDF); \
	elif command -v inotifywait > /dev/null 2>&1; then \
		echo "==> Watching for changes (using inotifywait)..."; \
		echo "Press Ctrl+C to stop"; \
		while true; do \
			inotifywait -e modify $(SOURCES) $(TABLES) 2>/dev/null && make $(PDF); \
		done; \
	else \
		echo "Error: Neither 'entr' nor 'inotifywait' found."; \
		echo "Install one of them to use watch mode:"; \
		echo "  - macOS: brew install entr"; \
		echo "  - Linux: apt-get install inotify-tools or dnf install entr"; \
		exit 1; \
	fi

# Help message
help:
	@echo "ACL Paper Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  make          - Compile $(MAIN).pdf (default)"
	@echo "  make copy-tables - Copy table files from parent directory"
	@echo "  make clean    - Remove auxiliary files (.aux, .log, etc.)"
	@echo "  make cleanall - Remove all generated files including PDF"
	@echo "  make watch    - Continuously compile on file changes"
	@echo "  make help     - Show this help message"
	@echo ""
	@echo "The PDF will be generated as: $(PDF)"
