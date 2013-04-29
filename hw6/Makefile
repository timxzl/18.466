all: hw6.pdf

%.pdf: %.dvi
	dvipdf $<

%.dvi: %.tex
	latex $< && latex $<
