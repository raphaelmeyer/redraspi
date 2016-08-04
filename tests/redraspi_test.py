from redraspi import redraspi
from unittest import mock

@mock.patch('redraspi.camera.Camera')
class TestRedRasPi:
    def test_does_not_take_a_picture_when_too_dark(self, camera_mock):
        with mock.patch('redraspi.sensors.Sensors') as Sensors:
            sensors = Sensors.return_value
            sensors.brightness.return_value = 0.69

            testee = redraspi.RedRasPi()
            testee.start()

            cam = camera_mock.return_value
            cam.take_picture.assert_not_called()

    def test_takes_a_picture_when_it_is_bright_enough(self, camera_mock):
        with mock.patch('redraspi.sensors.Sensors') as Sensors:
            sensors = Sensors.return_value
            sensors.brightness.return_value = 0.71

            testee = redraspi.RedRasPi()
            testee.start()

            cam = camera_mock.return_value
            cam.take_picture.assert_called_once_with()

