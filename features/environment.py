import datetime
from unittest import mock

def before_scenario(context, scenario):
    context.now = datetime.datetime(2023, 3, 23, 11, 23, 5)
    context.brightness = 123

    context.twitter_patch = mock.patch('twitter.Api')
    context.twitter_mock = context.twitter_patch.start()
    context.twitter_instance = context.twitter_mock.return_value

    context.camera_patch = mock.patch('redraspi.camera.Camera')
    context.camera_mock = context.camera_patch.start()
    context.camera_instance = context.camera_mock.return_value

    from redraspi import redraspi
    context.app = redraspi.RedRasPi()
    context.app.start()

def after_scenario(context, scenario):
    context.app.stop()
    context.camera_patch.stop()
    context.twitter_patch.stop()

