#!/usr/bin/python3
og_arr =  [2, 8, 9, 48, 8, 22, -12, 2]
nw_arr = []

for i in og_arr:
    x = i+2
    if x > 5:
        nw_arr.append(x)

print(og_arr)
print(nw_arr)