with open("salary.txt", "r", encoding="utf-8") as in_f:
    avg = 0
    salary = 0
    lines = 0
    while True:
        line = in_f.readline()
        if line == "":
            break
        salary = float(line.split()[1])
        avg += salary
        lines += 1
        if salary < 20000:
            print(line)
    print(f"average salary: {avg / lines}")
