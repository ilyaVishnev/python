class Clothes:
    expense = 0

    @property
    def expenses(self):
        return self.expense

    @expenses.setter
    def set_expense(self, expense):
        self.expense = expense

    def fabrics_consumption(self):
        pass

    def __add__(self, other):
        clothes = Clothes()
        # if self.expense is None:
        #     print("fd")
        # else:
        #     print("csd")
        clothes.expense = self.fabrics_consumption() + other.fabrics_consumption() if self.expense == 0 else \
            self.expense + other.fabrics_consumption()
        return clothes

    def __str__(self):
        return f"expense is {self.expense}"


class Coat(Clothes):

    def __init__(self, v):
        self.v = v

    @property
    def get_v(self):
        return self.v

    def fabrics_consumption(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, h):
        self.h = h

    @property
    def get_h(self):
        return self.h

    def fabrics_consumption(self):
        return 2 * self.h + 0.3


print(Coat(8) + Coat(9) + Suit(7))
