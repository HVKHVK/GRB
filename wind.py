import sys
import time
import os


def main():
    #grb_file = input("Please enter name of grb file (ex:2018020418_f000):")
    #latitude = input("Please enter latitude: ")
    #longitude = input("Please enter longitude: ")

	cmd_input = "cd /usr/src/GRB/; /usr/bin/grib2/wgrib2/wgrib2 2018020418_f000.grb -csv 2018020418_f000.csv"
    subprocess.call(cmd_input,shell=True)

main()
