with open("text_read.txt", "r") as in_f:
    lines = 0
    words = 0
    while True:
        line = in_f.readline()
        if line == "":
            break
        lines += 1
        words += len(line.split())
print(f"count of lines : {lines}\ncount of words : {words}")
