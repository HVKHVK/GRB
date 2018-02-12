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

    date = []
    coordinates = []
    meter = []
    speed = []
    direction = []

    for x in range(1,length):
        if(b'd=' == output[x:x+2]):
            date2 = output[x+2:x+5] + ' ' + output[x+6:x+8] + ' ' + output[x+9:x+11] + ' ' + output[x+12:x+14]
            date.append(date2)
            print date(i)

main()
