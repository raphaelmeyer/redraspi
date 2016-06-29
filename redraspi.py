#!/bin/python

def take_picture():
    import subprocess

    subprocess.run(['raspistill', '-o', '/tmp/picture.jpg', '-hf', '-vf', '-w', '256', '-h', '256', '-t', '1000'])

def main():
    import config
    import twitter

    api = twitter.Api(
            consumer_key = config.twitter.consumer_key,
            consumer_secret = config.twitter.consumer_secret,
            access_token_key = config.twitter.access_token,
            access_token_secret = config.twitter.access_secret,
            input_encoding = 'utf-8')

    take_picture()

    status = api.PostMedia(status = 'My first post. Weeha!', media='/tmp/picture.jpg')

    print(status)

if __name__ == "__main__":
    main()


