
import tweepy  # this will give an error if tweepy is not installed properly
from tweepy import OAuthHandler


# Twitter API credentials - https://apps.twitter.com/
consumer_key = 'luCMgoolgODpFH9rxcvLbRqYt'
consumer_secret = 'lW9fERVDfcgoq3aqVDYpbUNGkKUUFquwpQYrLvlaXzeekpvkgZ'
access_token  = '750950262098059268-riOExqjYPhUTJAe4OHW9F7aYfK2ljuQ'
access_token_secret = 'GE4K0zqwyBi50k5Ma3xFSP44zYd1HiM5ncL1gGaDscu5K'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

from tweepy import Stream
from tweepy.streaming import StreamListener

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('arabictweet.json', 'a') as f:  # change location here if you want
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())

# change the keyword here
twitter_stream.filter(track=['مكه'])

