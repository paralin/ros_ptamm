all:
	cd ptamm_com && make -j8
	cd ..
	cd ptamm && make -j8
	cd ..

clean: 
	cd ptamm && make clean 
	cd ..
	cd ptamm_com && make clean
	cd ..
	
	
distclean: 
	cd ptamm && make distclean 
	cd ..
	cd ptamm_com && make distclean
	cd ..
