n = int(input("Put a number between 1 and 12: "))
seasons = {tuple([12, 1, 2]): "Winter", tuple([3, 4, 5]): "Spring",
           tuple([6, 7, 8]): "Summer", tuple([9, 10, 11]): "Autumn"}
for el in seasons.keys():
    if n in el:
        print(seasons.get(el))
