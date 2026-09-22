#!/usr/bin/python3
string = str(input())
str_len = len(string)
i = 0
new_string = ""
for i in string:
    #print(c)
    if (i.isupper() == True):
        new_string += i.lower()
        #print(new_string)

    elif (i.islower() == True):
        new_string += i.upper()
        #print(new_string)
    else:
        new_string += i
print(new_string)