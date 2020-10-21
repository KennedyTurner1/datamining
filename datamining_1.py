import keys #keys.py
import tweepy as t

auth = t.OAuthHandler(keys.consumer_key, keys.consumer_secret) #prep to authenticate ourselves, creates an authentication object
auth.set_access_token(keys.access_token, keys.access_secret) #setting the tokens

api = t.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) #API object 

user = api.get_user("prattprattpratt")

print(user.name) #print the users name

print(user.description) #print bio

print(user.status.text) #print the latest tweet

print(user.followers_count) 

print(user.geo_enabled) #his location 

me = api.me

#print(me.name)

followers = []

cursor = t.Cursor(api.followers, screen_name='prattprattpratt') #an object

for follower in cursor.items(10):
    followers.append(follower.screen_name)

print(followers) 

friends = [] #who is chris following

cursor = t.Cursor(api.friends, screen_name='prattprattpratt') #an object

for friend in cursor.items(10):
    friends.append(friend.screen_name)

print(friends)

#returns tweets from the timeline of a specific account
chris_tweets = api.user_timeline(screen_name='prattprattpratt', count=5)

for tweet in chris_tweets:
    print(f"{tweet.user.screen_name}: {tweet.text}\n")

