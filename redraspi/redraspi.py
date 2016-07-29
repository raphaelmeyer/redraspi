#!/bin/python

class RedRasPi:
    def start(self):
        take_picture()

    def stop(self):
        pass

def take_picture():
    from redraspi import camera
    cam = camera.Camera()
    cam.take_picture()

def post_tweet():
    from settings import settings
    import twitter

    api = twitter.Api(
            consumer_key = settings.consumer_key,
            consumer_secret = settings.consumer_secret,
            access_token_key = settings.access_token,
            access_token_secret = settings.access_secret,
            input_encoding = 'utf-8')

    api.PostUpdate()

