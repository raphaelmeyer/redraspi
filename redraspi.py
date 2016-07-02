#!/bin/python

def take_picture():
    import subprocess

    subprocess.run(['raspistill', '-o', '/tmp/picture.jpg', '-hf', '-vf', '-w', '256', '-h', '256', '-t', '1000'])

def main():
    from settings import settings
    import twitter

    api = twitter.Api(
            consumer_key = settings.consumer_key,
            consumer_secret = settings.consumer_secret,
            access_token_key = settings.access_token,
            access_token_secret = settings.access_secret,
            input_encoding = 'utf-8')

    take_picture()

    #deprecated, use api.PostUpdate instead
    #status = api.PostMedia(status = 'My first post. Weeha!', media='/tmp/picture.jpg')
    #print(status)

if __name__ == "__main__":
    main()


