class Cell:

    def __init__(self, mesh_count):
        self.mesh_count = mesh_count

    def __add__(self, other):
        return Cell(self.mesh_count + other.mesh_count)

    def __sub__(self, other):
        if self.mesh_count - other.mesh_count <= 0:
            print("too few meshes")
            return
        return Cell(self.mesh_count - other.mesh_count)

    def __mul__(self, other):
        return Cell(self.mesh_count * other.mesh_count)

    def __truediv__(self, other):
        return Cell(self.mesh_count / other.mesh_count)

    def make_order(self, line):
        stars = list()
        i = 0
        while i != self.mesh_count:
            stars.append("*")
            i += 1
            if i % line == 0:
                stars.append("\\n")
        return "".join(stars)


c = Cell(12)
print(c.make_order(5))
