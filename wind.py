import sys
import time
import os
import subprocess, math
import argparse, csv

def main():
    filename = sys.argv[1]
    lan = sys.argv[2]
    lon = sys.argv[3]
    p = subprocess.Popen(['/usr/bin/grib2/wgrib2/wgrib2', filename, '-s', '-lon', lan, lon ], stdout=subprocess.PIPE)
    output = p.stdout.read().decode("utf-8")
    length = len(output)
    
    coordinates = lan + ' ' + lon
    
    date = []
    meter = []
    UGRD = []
    VGRD = []
    speed = []
    direction = []

    for x in range(1,length):
        if('d=' == output[x:x+2]):
            if ('UGRD' == output[x+13:x+17]):
                if('val=' == output[x+69:x+73]):
                    date.append(output[x+8:x+10] + '/' + output[x+6:x+8] + '/' + output[x+2:x+6] + ' ' + output[x+10:x+12] + ':00')
                    meter.append(output[x+18:x+21])
                    UGRD.append(output[x+73:x+79])
                elif ('val=' == output[x+70:x+74]):
                    date.append(output[x+8:x+10] + '/' + output[x+6:x+8] + '/' + output[x+2:x+6] + ' ' + output[x+10:x+12] + ':00')
                    meter.append(output[x+18:x+21])
                    UGRD.append(output[x+74:x+80])
            elif ('VGRD' == output[x+13:x+17]):
                if('val=' == output[x+69:x+73]):
                    date.append(output[x+8:x+10] + '/' + output[x+6:x+8] + '/' + output[x+2:x+6] + ' ' + output[x+10:x+12] + ':00')
                    meter.append(output[x+18:x+21])
                    VGRD.append(output[x+73:x+79])
                elif ('val=' == output[x+70:x+74]):
                    date.append(output[x+8:x+10] + '/' + output[x+6:x+8] + '/' + output[x+2:x+6] + ' ' + output[x+10:x+12] + ':00')
                    meter.append(output[x+18:x+21])
                    VGRD.append(output[x+74:x+80])


    for i in range(0,len(UGRD)):
        direction.append(57.29578*(math.atan2(float(UGRD[i]),float(VGRD[i])))+180)
        speed.append(math.sqrt(float(UGRD[i])*float(UGRD[i])+float(VGRD[i])*float(VGRD[i])))

    with open('output.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                        quotechar='', quoting=csv.QUOTE_MINIMAL)

        for i in range(0,len(UGRD)):
            print(date[i*2] + ' ' + coordinates + ' ' + meter[i*2] + ' ' + str(direction[i]) + ' ' + str(speed[i]) + '\n')
            spamwriter.writerow([str(date[i*2])]+[str(coordinates)]+[str(meter[i*2])]+[str(direction[i])]+[str(speed[i])])

main()


#DIRECTION=57.29578*(arctangent(UGRD,VGRD))+180.
#SPEED=SQRT(UGRD*UGRD+VGRD*VGRD)

#1:0:d=2018020418:UGRD:80 m above ground:anl::lon=30.000000,lat=36.000000,val=-6.21079\n2:3067:d=2018020418:VGRD:80 m above ground:anl::lon=30.000000,lat=36.000000,val=0.509568\n3:6134:d=2018020418:UGRD:100 m above ground:anl::lon=30.000000,lat=36.000000,val=-6.25109\n4:9201:d=2018020418:VGRD:100 m above ground:anl::lon=30.000000,lat=36.000000,val=0.5323\n'
