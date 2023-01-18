# QCXMS
A trial of using qcxms.

# Generate mol files by read in a txt file conaining multiple chemical smiles:
* Use the readSmileWriteCoord.py to generate the mol files. The result will be "n" mol files in n folders. python readSmileWriteCoord.py
# Use Nextflow to gerneate MS:
* Go to the folder that contain nxfl.nf and run "nextflow nxfl.nf". It will convert the mol files in each folder to coord file. And start the QCXMS process for each file.
