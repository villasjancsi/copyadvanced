#!/usr/bin/env python3

"""
Created by: Janos Villas
E-mail: villas_jancsi@windowslive.com
University of Debrecen
"""


import sys
import os
import time

DefaultBlockSize = 32768

def main():
    #Handling the error if user called the program with no/invalid parameters.
    if len(sys.argv) < 3:
        print("usage: {0} <source file> <destination file> [blocksize]".format(sys.argv[0]))
        exit(1)
    print("Beginning copy...")
    #Opening the source file for read
    with open(sys.argv[1], "r") as f1:
        #Opening the destination file for writing
        with open(sys.argv[2], "w") as f2:
            #Init variables
            totalbytes = os.path.getsize(sys.argv[1])
            blocksize = int(sys.argv[3] if len(sys.argv) == 4 else DefaultBlockSize)
            bytes = 0
            bytes_tmp = 0
            lastbytes = 0
            starttime = time.time()
            second = 0
            minute = 0
            speedunitlist = ["Bs", "KBs", "MBs", "GBs", "TBs"]
            speedunit = 0
            speed = 0
            #The copy-loop, which reads -blocksize- bytes from the source file
            #and writes it to destination file
            while True:
                byte = f1.read(blocksize)
                if byte == "":
                    break
                f2.write(byte)
                bytes += blocksize
                #Checking the time, and change variables for speed, eta, etc.
                if time.time() - starttime >= 0.5:
                    starttime = time.time()
                    bytes_tmp = lastbytes
                    lastbytes = bytes
                    speed = float(lastbytes-bytes_tmp)*2
                    speedunit = 0
                    while speed >= 1024 and speedunit < len(speedunitlist)-1:
                        speedunit += 1
                        speed /= 1024
                    second += 0.5
                    if second == 60:
                        minute += 1
                        second = 0
                #Writing to standard output, then flush
                sys.stdout.write("\r[{progressbar:50}] | {percentage:3}% | {speed:6.2f} {speedunit:3} | Time: {time_min:02}:{time_sec:02} | ETA: {eta_min:02}:{eta_sec:02}".format(\
                        progressbar=int(float(bytes)*100/totalbytes/2)*'*', \
                        percentage=int(float(bytes)*100/totalbytes), \
                        speed=speed, \
                        speedunit=speedunitlist[speedunit], \
                        time_min=minute, \
                        time_sec=int(second), \
                        eta_min=int((totalbytes-bytes)/(speed*(1024**speedunit))/60) if lastbytes - bytes_tmp > 0 else 0, \
                        eta_sec=int((totalbytes-bytes)/(speed*(1024**speedunit)))%60 if lastbytes - bytes_tmp > 0 else 0))
                sys.stdout.flush()
    print("\nDone!")
    exit(0)

#Working if this is the main program.
if __name__ == "__main__":
    main()
