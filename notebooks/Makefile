# sections 1-3 are managed under .teacher

NOTEBOOKS = $(shell git ls-files .teacher/[1-3]* [4-9]*)

all: book
.PHONY: all

include Makefile.book2

include Makefile.style2

NBNORMFLAGS = -l1 -s2 -t h1 -L License -S 'HTML\('
include Makefile.norm

include Makefile.prune
