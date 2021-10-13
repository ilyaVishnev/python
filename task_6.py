lessons = {}
with open("lessons.txt", "r", encoding="utf-8") as in_f:
    while True:
        line = in_f.readline().split(":")
        if len(line) < 2:
            break
        num = ""
        hours = 0
        for i in line[1]:
            if i.isdigit():
                num += i
            if i == "(":
                hours += int(num)
                num = ""
        lessons[line[0]] = hours
    print(lessons)
