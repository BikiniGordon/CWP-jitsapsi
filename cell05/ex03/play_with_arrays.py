#!/usr/bin/python3
og_arr = [2, 8, 9, 48, 8, 22, -12, 2]
nw_set = set([])

for i in og_arr:
    x = i + 2
    #nw_set.add(x)
    if x >= 10:
        nw_set.add(x)

print(og_arr)
print(nw_set)