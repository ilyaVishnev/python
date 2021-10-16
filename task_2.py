class Road:
    __length = ""
    __width = ""

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass_calculation(self, thick):
        return self.__width * self.__length * 25 * thick


road = Road(20, 5000)
print(road.mass_calculation(5))
