class Worker:
    name = ""
    surname = ""
    position = ""
    __income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, income):
        self.position = position
        self.name = name
        self.surname = surname
        self.__income = income


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._Worker__income


pos = Position("ilya", "vishnevskii", "developer", {"wage": 25000, "bonus": 35000})
print(pos.position)
print(pos.get_full_name())
print(pos.get_total_income())
