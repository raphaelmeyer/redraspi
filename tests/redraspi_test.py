from redraspi import redraspi
from unittest import mock
import unittest
import threading

@mock.patch('time.sleep', return_value=None)
@mock.patch('redraspi.redraspi.Main')
class TestRedRasPi(unittest.TestCase):

    def setUp(self):
        self.testee = redraspi.RedRasPi()
        self.testee_thread = threading.Thread(target=self.testee.start)

        self.loop_called = threading.Event()
        self.continue_loop = threading.Event()

    def tearDown(self):
        if self.testee_thread.is_alive():
            self.testee.stop()
            self.continue_loop.set()
            self.testee_thread.join(timeout=0.1)
            self.assertFalse(self.testee_thread.is_alive())

    def loop_sync(self):
        self.loop_called.set()
        self.continue_loop.wait()
        self.continue_loop.clear()

    def test_that_the_main_loop_is_called_periodically(self, Main, Time):
        main = Main.return_value
        main.loop.side_effect = self.loop_sync

        self.testee_thread.start()

        self.assertTrue(self.loop_called.wait(timeout=0.1))
        self.loop_called.clear()
        self.continue_loop.set()

        self.assertEqual(main.loop.call_count, 1)

        self.assertTrue(self.loop_called.wait(timeout=0.1))
        self.loop_called.clear()
        self.continue_loop.set()

        self.assertEqual(main.loop.call_count, 2)

    @unittest.skip("pending")
    def test_that_there_is_a_pause_of_100ms_between_each_main_loop_call(self, Main, Time):
        self.fail()

    @unittest.skip("pending")
    def test_that_the_main_loop_stops_when_shut_down(self, Main, Time):
        self.fail()

