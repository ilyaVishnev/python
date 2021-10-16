class Car:
    speed = 0
    color = ""
    name = ""
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Go")

    def stop(self):
        print("Stop")

    def turn(self, direction):
        print("is turning on " + direction)

    def show_speed(self):
        print(self.speed)


class TownCar(Car):

    def show_speed(self):
        print(self.speed if self.speed <= 60 else "speed limit exceeded")


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        print(self.speed if self.speed <= 40 else "speed limit exceeded")


class PoliceCar(Car):
    is_police = True


town_car = TownCar(70, "black", "bmw", False)
town_car.show_speed()

work_car = WorkCar(50, "white", "bmw", False)
work_car.show_speed()

police_car = PoliceCar(70, "red", "mercedes", True)
print(police_car.is_police)
