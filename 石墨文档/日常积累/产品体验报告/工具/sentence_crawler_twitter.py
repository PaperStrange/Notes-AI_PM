import tweepy


consumer_key = 'xxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class SimpleListener(tweepy.StreamListener):
    def on_status(self, status): 
        #code to run each time the stream receives a status
        print(status.text)

    def on_direct_message(self, status): 
        #code to run each time the stream receives a direct message
        print(status.text)
    
    def on_data(self, status):
        #code to run each time you receive some data (direct message, delete, profile update, status,...)
        print(status.text)

    def on_error(self, status_code):
        #code to run each time an error is received
        if status_code == 420:
            return 0
        else:
            return 1


tweepy_listener = SimpleListener()
tweepy_stream = tweepy.Stream(auth = api.auth, listener=tweepy_listener())
tweepy_stream.filter(track=['podcast'])