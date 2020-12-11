import os, sys, re

print('Hello World!')
# print(os.listdir('./day1'))
file_object  = open("./day3/input.txt", "r") 
# print(file_object.readlines())
# numbers_array = file_object.read().splitlines()
counter = 0
passwords = []
pos = 0;
for line in file_object:
    line = line.strip()
    print (line)
    print (pos%len(line))
    print(line[pos%len(line)])
    if (line[pos%len(line)]=='#'):
        counter+=1;
    pos += 3;
    # input = re.split("^([0-9]+)-([0-9]+) (.*): (.*)",line)
        
print (counter)
