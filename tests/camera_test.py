from redraspi import camera
from unittest import mock

@mock.patch('subprocess.run')
class TestCamera:

    def test_camera_calls_raspistill_to_take_a_picture(self, mock_run):
        cam = camera.Camera()
        cam.take_picture()

        assert mock_run.call_count == 1

        cmd = mock_run.call_args[0][0]
        assert cmd[0] == 'raspistill'

    def test_a_picture_should_be_256_by_256_pixels(self, mock_run):
        cam = camera.Camera()
        cam.take_picture()

        cmd = mock_run.call_args[0][0]
        assert '-w' in cmd
        assert '-h' in cmd
        assert cmd[cmd.index('-w') + 1] == '256'
        assert cmd[cmd.index('-h') + 1] == '256'

    def test_the_picture_should_be_stored_in_a_temporary_location_with_a_fixed_named(self, mock_run):
        cam = camera.Camera()
        cam.take_picture()

        cmd = mock_run.call_args[0][0]
        assert '-o' in cmd
        assert cmd[cmd.index('-o') + 1] == '/tmp/picture.jpg'

