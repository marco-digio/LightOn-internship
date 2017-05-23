# README #

### What is this repository for? ###

* This repository contains the code developed during my internship at LightOn
* Version 0.1

### How do I get set up? ###

To run the code, the following python libraries are needed:
* numpy
* scipy
* sklearn
* matplotlib
* time
* os

##### Script directory #####
To recover the plots of my internship final report, run the correspondent scripts. 
Example: 
`python script/QR_scripts.py`


Some scripts require real datasets, download them at:
* [SalinasA and Indian Pines datasets for NMF](http://www.ehu.eus/ccwintco/index.php?title=Hyperspectral_Remote_Sensing_Scenes)
* [ORL and Yale faces datasets for k-means](http://www.face-rec.org/databases/)

and put them in a directory called dataset.

##### Core directory #####
In the core directory, two tipes of files are present:
* main files contain basic functions to run the new algorithms (for example: QR.py). If you just want to use the algorithm, only these are the files that you need
* tools files that perform analysis of the correspondent algorithms and plot figures (for example QR_tools.py)

This core files are imported by the correspondent scripts files when executed.

# LightOn-internship
