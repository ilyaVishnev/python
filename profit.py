receipt = int(input("Введите выручку: "))
costs = int(input("Введите издержки: "))
if costs >= receipt:
    print("Пора закрывать контору 'Рога и Копыта'")
else:
    print("Всё пока что в порядке")
    p = int(input("Введите количество сотрудников: "))
    print(f"каждый сотрудник заработал для хозяина: {(receipt - costs) / p}")