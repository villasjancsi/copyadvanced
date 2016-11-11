Created by: Janos Villas, University of Debrecen, Faculty of Informatics, 11-11-2016

If you don't like the standard cp command, you can use it instead.
This is more human-friendly, than the default. 

Explaining the working:
 - It opens the source file for reading.
 - After that it opens the destination file for writing.
 - Than it can start it's process. If the user did not specified
   the blocksize, it will use 1024 (bytes) for a block.
 - It reads into the memory, then it writes to the destination file.
 - The more blocksize you give, the more memory will be used!
 - While we are doing it, the program will show us some information.

You will see these informations while you copy a file:
Progressbar, percentage, speed, elapsed time, and ETA.
Example output:
[**************************************************] | 100% |  33.80 MBs | Time: 00:04 | ETA: 00:00

I hope you enjoy!