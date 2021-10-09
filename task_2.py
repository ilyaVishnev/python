from random import randint

my_list = [randint(1, 100) for i in range(10)]
new_list = list()
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        new_list.append(my_list[i])
print(new_list)
