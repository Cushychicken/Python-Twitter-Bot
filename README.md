# Python-Twitter-Bot

# Installation
To use this Twitter bot, you need to have Python 3 installed on your system.

This bot also uses the `tweepy` module, which can be installed with pip using this command:

```shell
 $ pip install tweepy
```

# Setup Instructions

## Creating a Twitter Application

Twitter requires an Application be creatd through their Developer Portal. This can be through an existing account, or a new one. Creating a new account for your bot is recommended to prevent your personal Twitter account from getting banned.

To create a new application on Twitter, open this URL in your browser, and ffollow the instructions to join the developer program and create an App:

https://developer.twitter.com/apps

## Get Your API Access Credentials

Three bits of info from the Twitter App are required:

* a Consumer Key,
* a Consumer Secret, 
* an Access Token, 
* An Access Token Secret

3.Fill all details required to create the new app.After that ,click on "Key and Access Token" tab under app settings.You will get your app's Consumer Key (API Key , Consumer Secret (API Secret) .You also need to get Access Token and Access Token Secret of your app.We will use these valuse in next step.You need to generate Access Token for first time.

## Add your credentials to the App

Modify `credentials.py`, and copy/paste your app's details into the proper fields.

## Test Your Credentials (Optional)

A quick test of your app is to run `twitterbot_text.py`. This is a simple bot that will tweet each line of "The Zen of Python" as its own tweet.

Run this bot using this command:

```shell
 $ python twitterbot_text.py 
```
 
 ![Twitter Text Bot Screenshot](https://github.com/gauravssnl/Python-Twitter-Bot/blob/master/twitter%20text%20bot.png)

## Modifying The Bot

If you'd like the bot to send different text than "The Zen of Python", you can provide the bot with a different input file. 

You can do this by modifying `twitterbot_text.py`, and editing this line:

```python
my_file=open('sample.txt','r') 
```

You can also modify the sleep time of the bot to whatever you prefer. Default setting is 5 minutes / 300 seconds.


# Creating a Twitter bot which retweets, likes, and follows

The file `twitterbot_retweet.py` demonstrates a Twitter bot that:

* retweets tweets based on particular hastag (script provided here use #python ),
* likes tweets, and 
* follows the user who tweeted it .

The `config.py` file allows you to set desired parameters for the bot, such as `QUERY`, `LIKE`, and `FOLLOW`.  

Run the script with the following command:

```shell
$ python twitterbot_retweet.py
```


![Twitter Retweet Bot](https://github.com/gauravssnl/Python-Twitter-Bot/blob/master/twitter%20retweet%20bot.png)

You can use any desired hastag(such as #javascipt ) .Just edit hastag '#python' in config.py file with whatever you want.


10. You can also edit code if you do not want your bot to follow  users or you do not want your bot  to like tweets.


## Continuous Operation

Deploying the bot to a cloud service will allow it to run 24 hours a day.

Be mindful of sleep/delay settings if you choose to run the bot continuously. A generous sleep interval will minimize the odds of your account getting banned.






