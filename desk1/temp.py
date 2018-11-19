import sys
import os

file = open("associations.txt")
data = file.read()
lines = data.split("\n")
i = 1
for line in lines:
    if i%5==1:
        print(line)
    i = i + 1
