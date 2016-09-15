from redraspi import redraspi
from unittest import mock
import unittest

@mock.patch('redraspi.redraspi.Main')
class TestRedRasPi:

    def setup(self):
        self.testee = redraspi.RedRasPi()

    @unittest.skip("pending")
    def test_calls_main_loop_every_100ms(self, Main):
        self.fail()

    @unittest.skip("pending")
    def test_stops_main_loop_execution(self, Main):
        self.fail()

    def test_calls_main_loop_when_started(self, Main):
        self.testee.start()

        main = Main.return_value
        main.loop.assert_called_once_with()

