from itertools import cycle

abc = input("Put a line for cycling: ")
c = 0
for i in cycle(abc):
    c += 1
    if c == 13:
        break
    print(i)
