class Matrix:

    def __init__(self, array):
        self.array = array

    def __str__(self):
        field = ""
        for row in self.array:
            field += " ".join(map(str, row)) + "\n"
        return field

    def __add__(self, other):
        h = len(self.array[0])
        x = len(self.array)
        third_array = [[0 for i in range(len(self.array[0]))] for j in range(len(self.array))]
        for i, row in enumerate(self.array):
            for j, col in enumerate(row):
                third_array[i][j] = self.array[i][j] + other.array[i][j]
        return Matrix(third_array)


a = [[1, 2, 3], [4, 5, 6]]
b = [[7, 8, 9], [10, 11, 12]]
m1 = Matrix(a)
m2 = Matrix(b)
print(m1 + m2)
