from redraspi import sensors, camera

class Main:
    def __init__(self):
        self.sensors = sensors.Sensors()
        self.camera = camera.Camera()

    def loop(self):
        if self.sensors.brightness() > 0.7:
            self.take_picture()

    def take_picture(self):
        self.camera.take_picture()

class RedRasPi:
    def start(self):
        main = Main()
        main.loop()

    def stop(self):
        pass

