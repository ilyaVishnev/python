line = input("Put new entity as a line like \" key:value,key:value\" : ")
my_list = list()
i = 1
while line:
    my_dict = dict()
    my_tuple = (i, my_dict)
    my_line = line.split(",")
    for el in my_line:
        my_dict[el.split(":")[0]] = el.split(":")[1]
    my_list.append(my_tuple)
    line = input()
    i += 1
dict_res = dict()
for el in my_list:
    for k in el[1].keys():
        if k not in dict_res.keys():
            dict_res[k] = list()
        dict_res[k].append(el[1][k])
print(dict_res)
