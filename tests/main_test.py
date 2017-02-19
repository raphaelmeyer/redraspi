from redraspi import redraspi
from unittest import mock

@mock.patch('redraspi.sensors.Sensors')
@mock.patch('redraspi.camera.Camera')
class TestMain:

    def test_does_not_take_a_picture_when_too_dark(self, Camera, Sensors):
        testee = redraspi.Main()
        sensors = Sensors.return_value
        sensors.brightness.return_value = 0.69

        testee.loop()

        camera = Camera.return_value
        camera.take_picture.assert_not_called()

    def test_takes_a_picture_when_it_is_bright_enough(self, Camera, Sensors):
        testee = redraspi.Main()
        sensors = Sensors.return_value
        sensors.brightness.return_value = 0.71

        testee.loop()

        camera = Camera.return_value
        camera.take_picture.assert_called_once_with()
