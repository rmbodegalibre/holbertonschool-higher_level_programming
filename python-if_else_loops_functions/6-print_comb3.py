#!/usr/bin/python3
print("01", end="")
for i in range(102, 199):
    #print(i)
    if int(str(i)[2]) > int(str(i)[1]):
         print(", {}".format(str(i)[1:]), end="")
print("")
