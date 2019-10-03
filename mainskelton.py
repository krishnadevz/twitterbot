import tweepy
import time
CONSUMER_KEY="tkBz3ewGYoHivWKkyYcRfqk9z"
CONSUMER_SECRET="Dkwju8fPTU3LA0qt8zjCadmCPLL43DEpsQW1TglsddFXlgVIS3GH"
ACCESS_KEY="902905259231633408-1ETuKEku0dWcktANdTe7okfPzqP3Y3T"
ACCESS_SECRET="PVh7E3w3lF5jU7AU08OIAr2d69zjzRsBKcNb2LzBoNRZR"
#for checking timeline tweets
api.mentions_timeline()
mentions=api.mentions_timeline() #stored the mentions tweets ovehere
api = tweepy.api(auth, wait_on_rate_limit=True) #for avoiding rate limit exceed error
mentions[0].__dict__ #converted into the dictionary(python) 
mentions[0].__dict__.keys()
FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#twitterbot' in mention.full_text.lower():
            print('found #twitterbot!', flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name +
                    '#twitterbot back to you!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(1)
