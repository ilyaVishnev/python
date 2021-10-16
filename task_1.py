from time import sleep, perf_counter


class TrafficLight:
    __color = ""

    def running(self):
        self.__color = "red"
        print(self.__color)
        sleep(7)
        self.__color = "yellow"
        print(self.__color)
        sleep(2)
        self.__color = "green"
        print(self.__color)
        sleep(2)


light = TrafficLight()
light.running()
