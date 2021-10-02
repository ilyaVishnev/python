first = float(input("Put a positive float number: "))
while first < 0:
    first = float(input("Put a positive float number: "))
second = int(input("Put a negative integer number: "))
while second >= 0:
    second = int(input("Put a negative integer number: "))


def my_pow(a, b):
    c = 1
    for i in range(-b):
        c *= 1 / a
    return c


print(my_pow(first, second))
