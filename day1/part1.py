import os, sys

print('Hello World!')
# print(os.listdir('./day1'))
file_object  = open("./day1/input.txt", "r") 
# print(file_object.readlines())
# numbers_array = file_object.read().splitlines()
numbers_array = []
for line in file_object:
    numbers_array.append(int(line.strip('\n')))
numbers_array.sort()

# beginning
i = 0
j = len(numbers_array)-1
final_numbers = []
while (i<=j):
    print(f'i {i} {numbers_array[i]} j {j} {numbers_array[j]}')
    if (numbers_array[i]+numbers_array[j]) > 2020:
        print('greater')
        j-=1;
    elif (numbers_array[i]+numbers_array[j]) == 2020:
        print ('equal')
        final_numbers.append([numbers_array[i], numbers_array[j]])
        final_numbers.append(numbers_array[i]* numbers_array[j])
        i+=1;
    elif (numbers_array[i]+numbers_array[j]) < 2020:
        print('less')
        i+=1;
print(final_numbers)
print(numbers_array)