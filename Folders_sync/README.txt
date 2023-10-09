I implemented the script.py and added comments to illustrate the scope of each line of code.
The modification of files in replica and source should be done manually when the folders are 
identically to see how the program modifies/creates the files to have the replica folder 
syncronized to source folder.
This version of code is not working recursively, for example having subdirectories created inside
replica and source folders with another files and the files inside subdirectories to be modified too.


- How to run the code?

python3 script.py <path_to_the_folder>/Folders_sync/source <path_to_the_folder>/replica 
<path_to_the_folder>/logfile <timestamp_value_in_seconds>

