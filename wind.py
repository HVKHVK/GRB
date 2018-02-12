import sys
import time
import os
import subprocess, shlex
import argparse


def main():
    filename = sys.argv[1]
    lan = sys.argv[2]
    lon = sys.argv[3]
    meter = sys.argv[4]
    p = subprocess.Popen(['/usr/bin/grib2/wgrib2/wgrib2', filename, '-s', '-lon', lan, lon ], stdout=subprocess.PIPE)
    output = p.stdout.read()
    length = len(output)

    val1 = 'd='
    val2 = 'val='
    val3 = 'UGRD:'
    val4 = 'VGRD:'

    for x in range(1,length):
        if(val1 == output[x:x1]):
            print ('True')
           


main()
