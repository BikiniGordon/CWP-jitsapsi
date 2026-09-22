#!/usr/bin/python3
import sys
arg = len(sys.argv)
i = 0
n = 0
if arg == 1:
    #print(arg)
    while i in range(11):
        print("Table de " + str(i) + ":", end = " ")
        for n in range(10):
            print(i*n, end = " ")
            n = n + 1
        print(i*10,"")
        i = i + 1
else:
    print("none")