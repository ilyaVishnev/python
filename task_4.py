numbers = {"One": "один", "Two": "два", "Three": "три", "Four": "четыре"}
with open("en_rus.txt", "r", encoding="utf-8") as in_f:
    with open("rus_en.txt", "w", encoding="utf-8") as out_f:
        while True:
            line = in_f.readline().split("—")
            if len(line) < 2:
                break
            line_str = numbers[line[0]] + "—" + line[1]
            out_f.write(str(line_str))
