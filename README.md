# QCXMS
A trial of using qcxms.


* Use the readSmileWriteCoord.py to generate the mol files. The result will be "n" mol files in n folders. python readSmileWriteCoord.py
* Go to the folder that contain nxfl.nf and run "nextflow nxfl.nf". It will convert the mol files in each folder to coord file. And start the QCXMS process for each file.
