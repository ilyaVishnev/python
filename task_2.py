my_list = (input("enter the list items separate by space: ")).split()
for i, el in enumerate(my_list):
    if i % 2 != 0:
        my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
print(my_list)
