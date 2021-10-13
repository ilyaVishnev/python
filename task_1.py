with open("text.txt", "w") as out_f:
    while True:
        line = input("put your line here: ")
        if line == "":
            break
        out_f.write(line + "\n")
with open("text.txt", "r") as in_f:
    print(in_f.read())
