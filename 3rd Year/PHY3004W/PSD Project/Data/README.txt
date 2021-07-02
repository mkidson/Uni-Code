Directory contents:
	

	README.txt - this file... 
	readRaw.py - contains a class to open uncompressed files from QtDAQ
	exampleRead.py - demonstrates a basic implementation of readRaw
	Raw/ - directory in which you should keep your uncompressed QtDAQ files

Step 1: Change "fileName" in exampleRead.py to be the same as the uncompressed file.

Step 2: Run exampleRead.py. This should display the anode and dynode waveforms acquired 
	for each event (up to "maxEvents"). 

Step 3: Explore/edit/improve... 

You might want to:
	 - Subtract a baseline from the waveforms, then...
	 - For the dynode pulse you may want to extract the pulse height
	 - For the anode, define a reference point to align the pulses in time, then set 
	   a zero/start, short and long interval to calculate the short and long integrals
	  (Qs, Ql). A crude pulse shape parameter can be calculated as Qs/Ql.
	 - Try plotting histograms of dynode pulse height, anode long integral, and pulse 
	   shape parameter. 
	 - Try plotting a 2D histogram of dynode pulse height or anode long integral against 
	   pulse shape parameter.
	