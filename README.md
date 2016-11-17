# Copy advanced
The default cp command with some human-friendly feature.

### Usage
        python3 copyadvanced.py <sourcefile> <destinationfile> [blocksize]

### Blocksize
The size of the block. Reads *blocksize* byte(s) data from source file, and writes to destination file. 
**Warning!** *blocksize* should be less than the available memory.

### Features
* progressbar
* percentage
* speed
* elapsed time
* ETA

### Contributing
Your contributions are always welcome!

### Screenshot
![Screenshot](screenshot.png)

### Test

#### Testing environment
* File size: 536.870.912 bytes
* Computer
  * Kernel: Linux 3.13.0-34-generic x86_64
  * CPU: Intel(R) Core(TM) i3-2100 CPU @ 3.10GHz
  * RAM: 4 GB

#### Results
Blocksize | Time | Speed
--------- | ---- | -----
512 B | 04:11 | ~2MB/s
1024 B | 02:05 | ~4MB/s
4096 B | 00:31 | ~16MB/s
8192 B | 00:15 | ~32MB/s
