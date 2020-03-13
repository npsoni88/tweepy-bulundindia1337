# todo
# Exporting secrets
# CI CD
# Monitoring

import tweepy
import time
import os

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
key = os.getenv("key")
secret = os.getenv("secret")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

FILENAME = "records.txt"
def read_last_id(FILENAME):
    f = open(FILENAME, 'r')
    last_id = int(f.read().strip())
    f.close()
    return last_id

def write_last_id(FILENAME, last_retweet_id):
    r = open(FILENAME, 'w')
    r.write(str(last_retweet_id))
    r.close()


tweets = api.home_timeline(since_id=(read_last_id(FILENAME)))

def main():
    while True:
        for i in tweets:
            try:
                api.retweet(i.id)
            except tweepy.TweepError as e:
                print(e, i.id)
            try:
                api.create_favorite(i.id)
            except tweepy.TweepError as e:
                print(e, i.id)
            print("retweeteed! and liked ", i.id)
            write_last_id(FILENAME, i.id)
            time.sleep(20)
    

if __name__ == "__main__":
    main()
