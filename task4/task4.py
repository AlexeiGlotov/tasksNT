import sys

file_path = sys.argv[1]

arr_nums = []
arr_count = []
temp_summ = 0

with open(file_path, 'r') as file:
    for line in file:
        arr_nums.append(int(line.strip()))

for x in arr_nums: 
    for z in arr_nums:
        temp_summ = temp_summ + abs((x - z))

    arr_count.append(temp_summ)
    temp_summ = 0

print(min(arr_count))
