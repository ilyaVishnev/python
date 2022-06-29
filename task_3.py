class NotNumberException(Exception):
    pass


list_numbers = list()
while True:
    try:
        n = input("put your number here: ")
        if n == "stop":
            break
        if not n.isdigit():
            raise NotNumberException()
        list_numbers.append(int(n))
    except NotNumberException:
        print("not a digit, try again")
print(list_numbers)
