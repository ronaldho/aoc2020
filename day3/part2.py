import os, sys, re

print('Hello World!')
# print(os.listdir('./day1'))
file_object  = open("./day3/input.txt", "r") 
# print(file_object.readlines())
# numbers_array = file_object.read().splitlines()

counter = 1
passwords = []
# 
position_input = [[1,1], [3,1], [5,1], [7,1], [1,2]]
for x, y in position_input:
    pos_x = 0;
    pos_y = 0
    temp_counter=0
    for line in file_object:
        line = line.strip()
        # print (line)
        # print (pos%len(line))
        
        print(f'pos_x {pos_x} pos_y {pos_y} {line[pos_x%len(line)]}')
        if (pos_y % y != 0 ):
            print ('skipping')
            pos_y += 1
            continue;
        if (line[pos_x%len(line)]=='#'):
            print ('adding')
            temp_counter+=1;
        pos_x += x;
        pos_y += 1
        
    print (temp_counter) 
    counter *= temp_counter
    file_object.seek(0) #reset line
    # input = re.split("^([0-9]+)-([0-9]+) (.*): (.*)",line)
        
print (f'final {counter}') 
