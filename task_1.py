def dev_two_args(div1, div2):
    return div1 / div2


divisible = int(input("put integer divisible: "))
divisor = int(input("put integer divisor: "))
while divisor == 0:
    print("divisor shouldn't be a null")
    divisor = int(input("put integer divisor: "))
print(dev_two_args(divisible, divisor))
