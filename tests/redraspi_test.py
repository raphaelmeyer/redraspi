from redraspi import redraspi
from unittest import mock
import unittest

@mock.patch('time.sleep', return_value=None)
@mock.patch('redraspi.redraspi.Main')
class TestRedRasPi(unittest.TestCase):

    def setUp(self):
        self.testee = redraspi.RedRasPi()

    @unittest.skip("pending")
    def test_that_the_main_loop_is_called_periodically(self, Main, Time):
        assert False

    @unittest.skip("pending")
    def test_that_there_is_a_pause_of_100ms_between_each_main_loop_call(self, Main, Time):
        assert False

    # to be removed
    def test_calls_main_loop_when_started(self, Main, Time):
        self.testee.start()

        main = Main.return_value
        main.loop.assert_called_once_with()

