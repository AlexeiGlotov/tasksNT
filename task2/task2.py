import sys

file_path_coords = sys.argv[1]
file_path_point = sys.argv[2]

arr_coords = []
arr_point = []

with open(file_path_coords, 'r') as file:
    for line in file:
        arr_coords.append(line.strip())


with open(file_path_point, 'r') as file:
    for line in file:
        arr_point.append(line.strip())


coords_x = float(arr_coords[0].split()[0])
coords_y = float(arr_coords[0].split()[1])

for c in arr_point:
    point_x = float(c.split()[0])
    point_y = float(c.split()[1])

    a = pow(point_x - coords_x,2) + pow(point_y - coords_y,2)

    b = pow(int(arr_coords[1]),2)

    if a < b:
        print('1') # Внутри
    elif a > b:
        print('2') # Снаружи
    elif a == b:
        print('0') # На окружности