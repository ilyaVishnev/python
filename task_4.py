from random import randint

my_list = [randint(1, 10) for i in range(10)]
print(my_list)
unique_el = list()
repeat_el = list()
for el in my_list:
    if el in repeat_el:
        continue
    if el in unique_el:
        unique_el.remove(el)
        repeat_el.append(el)
        continue
    unique_el.append(el)
print(unique_el)
