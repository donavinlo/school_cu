import snscrape.modules.twitter as sntwitter
import pandas as pd
import json

#method to gather tweets
def tweet_scraper(query, lim=10):
    """
        Gather tweets based of of a given query. Returns a json object that we can dump

        Attributes of JSON object are:

        Text: the text of the tweet
        user_at: the @ name of the twitter account
        user_id: ID given to that specific user
        user_verified: If the account is a verified account
        user_followers: the follower count of the person that tweeted
        tweet_count: the total amount of tweets the account has made in its lifespan
        mentioned_users: a list of the @name and their id for each user mentioned in the given tweet

    """
    tweets = []

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) == lim:
            break
        else:
            mentioned_users = [(mentioned.username, mentioned.id) for mentioned in tweet.mentionedUsers ] #get ID and @ of each account mentioned

            tweets.append(
                {"text": tweet.content, 
                "user_at": tweet.user.username, 
                "user_id": tweet.user.id, 
                "user_verified": tweet.user.verified,
                "user_followers": tweet.user.followersCount,
                "tweet_count": tweet.user.statusesCount,
                "mentioned_users": mentioned_users})
    
    return tweets

############ Aaron Rodgers
query_string = '("Aaron OR Rodgers" OR @AaronRodgers12) -Contract -Davante -@tae15adams until:2022-07-25 since:2022-07-01 -filter:retweets -filter:replies lang:en'
LIMIT = 1000
arod = tweet_scraper(query_string, LIMIT)

## save as JSON object for multiple uses
with open('data/arod_tweets.json', 'w') as json_file:
    json.dump(arod, json_file, sort_keys=True, indent=1)