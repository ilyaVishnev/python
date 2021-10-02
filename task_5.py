print("if you like to stop - type letter \"n\"")
my_sum = 0
run = True
while run:
    line = input("put your numbers separated by space here: ")
    my_list = line.split()
    try:
        for el in my_list:
            if el == "n":
                run = False
                break
            my_sum += int(el)
        print(my_sum)
    except ValueError:
        print("not a number")
        break
