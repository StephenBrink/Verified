from tweepy import OAuthHandler
from IPython.core.page import page
from settings import *
import tweepy, json, sys, random, discord, time


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
    
api = tweepy.API(auth, wait_on_rate_limit=True)
target = 'hanaflorencia'
user = api.get_user(target)
followers = []

print(user)

if user._json['verified']:
    print(user._json['name'] + ' is verified!')
else:
    print(user._json['name'] + ' is not verified')\

for page in tweepy.Cursor(api.followers, screen_name=target).pages():
    followers.extend(page)
    #time.sleep(60)
    
print(len(followers))

        