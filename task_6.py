from itertools import count

n = int(input("Put a initial number :"))
for i in count(n):
    if i % 20 == 0:
        break
    else:
        print(i)
