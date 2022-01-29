import tweepy
from time import sleep
from credentials import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret,
    bearer_token=bearer_token
)

print("Retweet/Like/Follow Bot")
print()
print("Bot Settings")
print("Like Tweets :", LIKE)
print("Follow users :", FOLLOW)
print()

response = client.search_recent_tweets(
        QUERY, 
        max_results=20,
        expansions=["attachments.media_keys", "author_id"]
)

# In this case, the data field of the Response returned is a list of Tweet
# objects
tweets = response.data

# You can then access those objects in the includes Response field
includes = response.includes
users = includes["users"]

# An efficient way of matching expanded objects to each data object is to
# create a dictionary of each type of expanded object, with IDs as keys
users = {user["id"]: user for user in users}
for tweet in tweets:
    if users[tweet.author_id].username != 'RTLjobs':
        client.retweet(tweet.id)
        print("Retweeted " + str(tweet.id) + " by " + users[tweet.author_id].username)
        if LIKE:
            client.like(tweet.id)

        if FOLLOW :
            try:
                client.follow(tweet.author_id)
            except:
                pass

        sleep(1)

