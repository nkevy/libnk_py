============
Nkecon 
===========

Nkecon is a package containing tools to help with personal
finance and or to reasarch economic topics. A typical 
useage looks like:
	
	#!/usr/bin/env python

	from nkecon import Mtable
	
	mt = Mtable("./my_csv.csv")
	mt.complete_table()
	mt.export("my_completed.csv")

note: The above does not follow python indenting and is thus only a model.
