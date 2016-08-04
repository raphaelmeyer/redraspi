#!/bin/python

from redraspi import sensors, camera

class RedRasPi:
    def start(self):
        sens = sensors.Sensors()
        if sens.brightness() > 0.7:
            take_picture()

    def stop(self):
        pass

def take_picture():
    cam = camera.Camera()
    cam.take_picture()

