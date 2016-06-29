import config
import twitter

def main():
    api = twitter.Api(
            consumer_key = config.twitter.consumer_key,
            consumer_secret = config.twitter.consumer_secret,
            access_token_key = config.twitter.access_token,
            access_token_secret = config.twitter.access_secret,
            input_encoding = 'utf-8')

    print(api.GetUserTimeline(screen_name='pimoroni'.encode()))


if __name__ == "__main__":
    main()


