a = int(input("Введите количество км для первого дня: "))
b = int(input("Введите количество км которое нужно пройти : "))
n = 1
while a < b:
    a += 0.1 * a
    n += 1
print(f"Итого пробежал :{n}")
