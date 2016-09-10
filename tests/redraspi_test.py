from redraspi import redraspi
from unittest import mock

@mock.patch('redraspi.redraspi.Main')
class TestRedRasPi:

    def setup(self):
        self.testee = redraspi.RedRasPi()

    def test_calls_main_loop_when_started(self, Main):
        self.testee.start()

        main = Main.return_value
        main.loop.assert_called_once_with()

