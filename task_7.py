def fact(n):
    fact_list = list()
    for i in range(n):
        if i == 0:
            fact_list.insert(0, 1)
        else:
            fact_list.insert(i, (i + 1) * fact_list[i - 1])
        yield fact_list[i]


number = int(input("Put the number: "))
for j in fact(number):
    print(j)
