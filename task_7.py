import json

firms = {}
avg = 0
with open("task_7.txt", "r") as in_f:
    while True:
        line = in_f.readline().split()
        if len(line) < 4:
            break
        profit = int(line[2]) - int(line[3])
        avg += profit if profit > 0 else 0
        firms[line[0]] = profit
my_list = [firms, {"average_profit": avg}]
with open("task_7_json.txt", "w") as json_f:
    json.dump(my_list, json_f)
