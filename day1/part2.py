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
    if (numbers_array[i]+numbers_array[j]) >= 2020:
        print('greater')
        j-=1;
    elif (numbers_array[i]+numbers_array[j]) < 2020:
        print('less')
        k = 0;
        while (k < len(numbers_array)-1):
            sum = (numbers_array[i]+numbers_array[j]+numbers_array[k])
            print(f'i {i} {numbers_array[i]} j {j} {numbers_array[j]} k {k} {numbers_array[k]} sum {sum}')
            temp_i = i;
            if sum == 2020:
                final_numbers.append([numbers_array[i], numbers_array[j], numbers_array[k]])
                final_numbers.append(numbers_array[i]* numbers_array[j]*numbers_array[k])
            elif (sum >= 2020):
                while temp_i > 0:
                    if (numbers_array[temp_i]+numbers_array[j]+numbers_array[k]) == 2020:
                        final_numbers.append([numbers_array[temp_i], numbers_array[j], numbers_array[k]])
                        final_numbers.append(numbers_array[temp_i]* numbers_array[j]*numbers_array[k])
                    temp_i -= 1
            k+=1
        i+=1;
        
print(final_numbers)
print(numbers_array)