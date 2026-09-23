#!/usr/bin/python3
import sys

def downcase(s):
    return s.lower()

if (len(sys.argv)-1 <= 0):
    print("none")
else:
    for i in range(1, len(sys.argv)):
        print(downcase(sys.argv[i]))