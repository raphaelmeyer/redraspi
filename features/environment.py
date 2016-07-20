import datetime
from unittest import mock

def before_scenario(context, scenario):
    context.now = datetime.datetime(2023, 3, 23, 11, 23, 5)
    context.brightness = 123

    context.twitter_patch = mock.patch('twitter.Api')
    context.twitter_mock = context.twitter_patch.start()
    context.twitter_instance = context.twitter_mock.return_value

def after_scenario(context, scenario):
    context.twitter_patch.stop()

