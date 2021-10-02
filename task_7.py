import task_6

line = input("put a line from lowercase words separated by space: ")
new_line = line.split()
for i, w in enumerate(new_line):
    new_line[i] = task_6.int_func(w)
print(" ".join(new_line))
