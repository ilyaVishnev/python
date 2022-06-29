from abc import abstractmethod


class WareHouse:
    count = {"Printer": list(), "Scanner": list(), "Copier": list()}

    def add_to_warehouse(self, eq):
        eq.validate()
        if isinstance(eq, Printer):
            self.count["Printer"].append(eq)
        if isinstance(eq, Scanner):
            self.count["Scanner"].append(eq)
        if isinstance(eq, Copier):
            self.count["Copier"].append(eq)

    def __str__(self):
        return ' '.join(map(str, self.count['Printer'])) + ' '.join(map(str, self.count['Scanner'])) + ' '.join(
            map(str, self.count['Copier']))


class Equipment:

    def __init__(self, price, size):
        self.price = price
        self.size = size

    @abstractmethod
    def validate(self):
        pass


class Printer(Equipment):

    def __init__(self, price, size, type_pr):
        super(Printer, self).__init__(price, size)
        self.type_pr = type_pr

    def validate(self):
        if not (self.type_pr == "laser" or self.type_pr == "jet"):
            raise Exception("wrong type of printer")

    def __str__(self):
        return f" printers -> price: {self.price} size: {self.size} type: {self.type_pr}"


class Scanner(Equipment):
    def __init__(self, price, size, diagonal):
        super(Scanner, self).__init__(price, size)
        self.diagonal = diagonal

    def validate(self):
        if not (int(self.diagonal) < 50 or int(self.diagonal) > 20):
            raise Exception("wrong diagonal of scanner")

    def __str__(self):
        return f" scanners -> price: {self.price} size: {self.size} diagonal: {self.diagonal}"


class Copier(Equipment):

    def __init__(self, price, size, count_of_cartridges):
        super(Copier, self).__init__(price, size)
        self.count_of_cartridges = count_of_cartridges

    def validate(self):
        if not (int(self.size) < 500 or int(self.size) > 200):
            raise Exception("wrong size of copier")

    def __str__(self):
        return f" copiers -> price: {self.price} size: {self.size} count_of_cartridges: {self.count_of_cartridges}"


p = Printer(100, 350, "laser")
s = Scanner(130, 345, 30)
c = Copier(300, 400, 12)
w = WareHouse()
w.add_to_warehouse(p)
w.add_to_warehouse(s)
w.add_to_warehouse(c)
print(w)
