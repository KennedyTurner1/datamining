import keys #keys.py
import tweepy as t
import json
from wordcloud import WordCloud 

auth = t.OAuthHandler(keys.consumer_key, keys.consumer_secret) #prep to authenticate ourselves, creates an authentication object
auth.set_access_token(keys.access_token, keys.access_secret) #setting the tokens

api = t.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) #API object 

#tweepy has a search method to search for a query or a trending topic
#large volume, only what's in the last 7 days
'''
tweets = api.search(q='vote', count=3)

print(tweets)

for tweet in tweets:
    print(tweet)
    print(f"{tweet.user.screen_name} : {tweet.text}\n")

tweets = api.search(q='#collegefootball', count=2)

for tweet in tweets:
    print(tweet)
    print(f"{tweet.user.screen_name} : {tweet.text}\n")


#places with trending topics
#returns  list of dictionaries of the places that are trending

trends_available = api.trends_available() 

print(len(trends_available))

print(trends_available[:3]) #print the first item in the list, a dictionary 


world_trends = api.trends_place(id=1) #worldwide woeid

#print(world_trends)

outfile = open("world_trends.json", 'w')

json.dump(world_trends, outfile, indent=5) #dump contents into the outfile and indent it

trends_list = [trend for trend in world_trends[0]["trends"]] #making a list of dictionaries

#print(trends_list)

trends_list = [trend for trend in trends_list if trend['tweet_volume']] #the volume is either null or not null

from operator import itemgetter

trends_list.sort(key=itemgetter("tweet_volume"), reverse=True)

print(trends_list[:5])

for trend in trends_list[:5]: #for dictionary in the list
    print(trend['name']) #take the dictionary and find the key

#trending topics in NYC

nyc_trends = api.trends_place(id=2459115)

outfile = open("nyc_trends.json", 'w')

json.dump(nyc_trends, outfile, indent=5) #dump contents into the outfile and indent it

trends_list = nyc_trends[0]["trends"] #creating a list of dictionaries 

trends_list = [trend for trend in trends_list if trend['tweet_volume']] #for dictionary in the list 

nyc_dict = {}

for trend in trends_list:
    key = trend['name']
    value = trend['tweet_volume']
    nyc_dict[key] = value

wordcloud = WordCloud(
    width=1600,
    height=900,
    prefer_horizontal=0.5,
    min_font_size=10,
    colormap='prism',
    background_color='white'
)

wordcloud = wordcloud.fit_words(nyc_dict)

wordcloud = wordcloud.to_file("TrendingTwitter_Fall2020.png")
'''




