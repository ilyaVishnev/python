my_list = [7, 5, 3, 3, 2]
n = int(input("Put your number: "))
for i, el in enumerate(my_list):
    if n > el:
        my_list.insert(i, n)
        break
    if i == len(my_list) - 1:
        my_list.append(n)
        break
print(my_list)
