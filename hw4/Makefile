all: hw4.pdf

%.pdf: %.dvi
	dvipdf $<

%.dvi: %.tex
	latex $< && latex $<
