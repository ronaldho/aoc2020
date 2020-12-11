import os, sys, re

print('Hello World!')
# print(os.listdir('./day1'))
file_object  = open("./day2/input.txt", "r") 
# print(file_object.readlines())
# numbers_array = file_object.read().splitlines()
counter = 0
passwords = []
for line in file_object:
    line = line.strip()
    print (line)
    # input = re.split("^([0-9]+)-([0-9]+) (.*): (.*)",line)
    input = re.search("^([0-9]+)-([0-9]+) (.*): (.*)",line).groups()
    # input = input[0]
    print (input)
    # result = re.search(f"{input[2]}{{{input[0]},{input[1]}}}", input[3])
    count = input[3].count(input[2])
    if count>=int(input[0]) and count <= int(input[1]):
        counter+=1
        
print (counter)
