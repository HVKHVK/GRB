import sys
import time
import os
import subprocess, shlex


def main():
    #filename = sys.argv[1]
    #lan = sys.argv[2]
    #lon = sys.argv[3]
    #meter = sys.argv[4]
    command_line = input()
    args = shlex.split(command_line)
    print(args);
    p = subprocess.Popen(args)

main()
