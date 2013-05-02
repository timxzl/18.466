all: midterm2.pdf

%.pdf: %.dvi
	dvipdf $<

%.dvi: %.tex prelude.tex
	latex $<
