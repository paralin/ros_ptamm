all:
	cd thirdparty && make
	make -j8 -f Makefile_ptamm

clean:
	make -j8 -f Makefile_ptamm clean

.DEFAULT:
	cd thirdparty && make $@
	make -j8 -f Makefile_ptamm $@


