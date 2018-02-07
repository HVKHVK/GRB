import sys
import time
import os
import subprocess


def enter():
	subprocess.call("cd /usr/src/GRB/; /usr/bin/grib2/wgrib2/wgrib2 2018020418_f000.grb -csv 2018020418_f000.csv" ,shell=True)
def main():
   	grb_file = input("Please enter name of grb file (ex:2018020418_f000): ")
	enter()

main()
