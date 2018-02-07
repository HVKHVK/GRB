import sys
import time
import os
import subprocess


def main():
    #grb_file = input("Please enter name of grb file (ex:2018020418_f000):")
    #latitude = input("Please enter latitude: ")
    #longitude = input("Please enter longitude: ")
	#cmd_input = 'cd /usr/src/GRB/; /usr/bin/grib2/wgrib2/wgrib2 2018020418_f000.grb -csv 2018020418_f000.csv'

	#command = ['cd']
	#command.append('/usr/src/GRB/;') 
	#command.append('/usr/bin/grib2/wgrib2/wgrib2')
	#command.append('2018020418_f000.grb')
	#command.append('-csv')
	#command.append('2018020418_f000.csv')
    #(out,err) =subprocess.Popen(command,stdout=subprocess.PIPE).communicate()
 	subprocess.call(["ls", "-l"]) 

main()
