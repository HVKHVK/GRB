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
    output = p.stdout.read().decode("utf-8")
    length = len(output)

    date = []
    coordinates = []
    meter = []
    speed = []
    direction = []

    for x in range(1,length):
        if('d=' == output[x:x+2]):
            date2 = output[x+8:x+10] + '/' + output[x+6:x+8] + '/' + output[x+2:x+6] + ' ' + output[x+10:x+12] + ':00'
            date.append(date2)
            #print (date[0],)

    print (date[0],date[1],date[2],date[3])
main()
