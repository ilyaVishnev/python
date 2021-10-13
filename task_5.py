from random import randint

with open("numbers.txt", "w+") as f_obj:
    my_list = [str(randint(0, i)) for i in range(10)]
    line = " ".join(my_list)
    f_obj.write(line)
    f_obj.seek(0)
    print(sum([int(i) for i in f_obj.readline().split(" ")]))
