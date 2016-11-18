# group7rbm
Exercise Task of Group7 - CS-E4050 2016

The requirements for the exercise are in: 
https://mycourses.aalto.fi/pluginfile.php/387827/mod_resource/content/2/Exercises-StructuredProbabilisticModelsForDeepLearning.pdf

The original source code of rbm.py is from:
http://deeplearning.net/tutorial/rbm.html

Directory hierarcy is as suggested in slide 29/32 of session3slides.pdf
https://mycourses.aalto.fi/pluginfile.php/359772/mod_resource/content/5/session3slides.pdf

"
# DIRECTORY data
holds input data to the algorithms (e.g. MNIST data).

# DIRECTORY code 		
contains the main codes (which are Python-files).

# DIRECTORY configFiles
configuration files for specifying (varying) experiment details (such as hyperparameter values), inputs to the main codes
results the experiment results are written to subdirectories specified in the
configuration files; have matching names with the configuration file name
and the results directory name.

# DIRECTORY submitFiles	
shell-scripts for running the experiments; e.g. start an experiment using some Python-code with configurations read as input from a configuration file; have matching naming with configuration files (in terms of the prefix,
etc.)

# DIRECTORY experiments	
describes the experiments conducted, started by running the submitFiles
"

