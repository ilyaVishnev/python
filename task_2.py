class DoNotDivideByZeroException(ZeroDivisionError):
    pass


try:
    divisible = int(input("put a divisible: "))
    divisor = int(input("put a divisor: "))
    if divisor == 0:
       raise DoNotDivideByZeroException()
    print(f"result is {divisible / divisor}")
except DoNotDivideByZeroException:
    print("don't do it again")
