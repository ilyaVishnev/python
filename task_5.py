class Stationery:
    title = ""

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        print(f"написать ручкой {self.title}")


class Pencil(Stationery):

    def draw(self):
        print(f"рисунок карандашом {self.title}")


class Handle(Stationery):

    def draw(self):
        print(f"закрашиваем маркером {self.title}")


pen = Pen("имя")
pen.draw()

pencil = Pencil("автопортрета")
pencil.draw()

handle = Handle("стену")
handle.draw()
