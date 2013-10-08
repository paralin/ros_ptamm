all:
	cd thirdparty && make
	make -j8 -f Makefile_ptamm

.DEFAULT:
	cd thirdparty && make $@
	make -j8 -f Makefile_ptamm $@


