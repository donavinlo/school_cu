import json
import configparser
import time
import tweepy


#Secure Authentication
config = configparser.ConfigParser()
config.read("config.ini")
API_KEY = config['twitter_api']['api_key']
API_SECRET = config['twitter_api']['api_secret']
ACCESS_TOKEN = config['twitter_api']['access_token']
ACCESS_TOKEN_SECRET = config['twitter_api']['access_token_secret']

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

#Get my public Tweets and people I follow

public_tweets = api.home_timeline()
