import sys
import time
import os
import subprocess, shlex
import argparse


def main():
    filename = sys.argv[1]
    lan = sys.argv[2]
    lon = sys.argv[3]
    p = subprocess.Popen(['/usr/bin/grib2/wgrib2/wgrib2', filename, '-s', '-lon', lan, lon ], stdout=subprocess.PIPE)
    output = p.stdout.read()
    length = len(output)

    for x in range(1,length):
        if(b'd=' == output[x:x+2]):
            print (output[x+3:x+13])
           


main()
