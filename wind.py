import sys, os, time
import subprocess, math
import argparse, csv

def main():
    filename = sys.argv[1]
    lat = sys.argv[2]
    lon = sys.argv[3]
    p = subprocess.Popen(['/usr/bin/grib2/wgrib2/wgrib2', filename, '-s', '-lon', lat, lon ], stdout=subprocess.PIPE)
    output = p.stdout.read().decode("utf-8")
    length = len(output)
    
    coordinates = lat + ' ' + lon
    
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
        writer = csv.writer(csvfile)
        
        for i in range(0,len(UGRD)):
            writer.writerow([str(date[i*2])]+[str(coordinates)]+[str(meter[i*2])]+[str(direction[i])]+[str(speed[i])])

main()
#DIRECTION=57.29578*(arctangent(UGRD,VGRD))+180
#SPEED=SQRT(UGRD*UGRD+VGRD*VGRD)


