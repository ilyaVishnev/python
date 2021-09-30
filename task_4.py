words = input("Put some words separated by space: ").split()
for i, w in enumerate(words):
    print(i + 1, (w, w[:10])[len(w) > 10])
