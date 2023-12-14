import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

first  = 1
finaly = ''
while True:

    finaly += str(first)
    first = 1 + (first + m - 2) % n
    
    if first == 1:
        break

print(finaly)