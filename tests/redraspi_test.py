from redraspi import redraspi
from unittest import mock

@mock.patch('redraspi.camera.Camera')
class TestRedRasPi:
    def test_takes_a_picture(self, camera_mock):
        testee = redraspi.RedRasPi()
        testee.start()

        cam = camera_mock.return_value
        cam.take_picture.assert_called_once_with()

