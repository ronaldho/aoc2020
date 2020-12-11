import os, sys, re

print('Hello World!')
# print(os.listdir('./day1'))
file_object  = open("./day2/input.txt", "r") 
# print(file_object.readlines())
# numbers_array = file_object.read().splitlines()
counter = 0
passwords = []
# ('6', '7', 'c', 'xkdzcscg')
for line in file_object:
    line = line.strip()
    print (line)
    # input = re.split("^([0-9]+)-([0-9]+) (.*): (.*)",line)
    input = re.search("^([0-9]+)-([0-9]+) (.*): (.*)",line).groups()
    # input = input[0]
    # print (input[3][0])
    print (f'char at {input[0]} is {input[3][int(input[0])-1]}')
    print (f'char at {input[1]} is {input[3][int(input[1])-1]}')
    print(input[2])
    if ((input[3][int(input[0])-1] == input[2]) ^ (input[3][int(input[1])-1] == input[2])):
        print('matched')
        counter +=1

        
print (counter)
