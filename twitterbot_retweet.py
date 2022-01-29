import tweepy
from time import sleep
from credentials import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME
from datetime import datetime


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

while True:
    expansions=["attachments.media_keys", "author_id"]
    response = client.search_recent_tweets(
            QUERY, 
            max_results=20,
            expansions=expansions
    )

    # Returns list of Tweet objects
    tweets = response.data

    includes = response.includes
    users = includes["users"]

    # creates dict of each type of expanded object, with IDs as keys
    users = {user["id"]: user for user in users}
    for tweet in tweets:
        if users[tweet.author_id].username != 'RTLjobs':
            client.retweet(tweet.id)
            print("Retweeted " + str(tweet.id) + " by " + users[tweet.author_id].username)
            if LIKE:
                client.like(tweet.id)

            if FOLLOW:
                try:
                    client.follow_user(tweet.author_id)
                except:
                    pass

            sleep(1) # Politeness interval

    # Sleep until next retweet iteration
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    print("Check complete at " + current_time + "; next run in 15 mins...")
    sleep(SLEEP_TIME)

