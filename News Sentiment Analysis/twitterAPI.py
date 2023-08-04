import tweepy
import pandas as pd
import configparser

# * read configuration

config = configparser.ConfigParser()
config.read('config.ini')

API_Key = config['Twitter']['API_Key']
API_Secret = config['Twitter']['API_Key_Secret']
acessToken = config['Twitter']['access_token']
acessSecretToken = config['Twitter']['access_secret_token']

# print(API_Key, API_Secret, acessToken, acessToken)

auth = tweepy.OAuth1UserHandler(API_Key,API_Secret)

auth.set_access_token(acessToken,acessSecretToken)

api = tweepy.API(auth)

numberOfTweets = 100

# * Getting data from news channels (Just uncomment the cursor and run the following)

# cursor = tweepy.Cursor(api.user_timeline,id='@CNN',tweet_mode="extended").items(numberOfTweets)

# cursor = tweepy.Cursor(api.user_timeline,id='@FoxNews',tweet_mode="extended").items(numberOfTweets)

# cursor = tweepy.Cursor(api.user_timeline,id='@BBCWorld',tweet_mode="extended").items(numberOfTweets)

# cursor = tweepy.Cursor(api.user_timeline,id='@SkyNews',tweet_mode="extended").items(numberOfTweets)

# tweetText = []
# tweetLikes = []
# time = []

# printing data
# for i in cursor:
#     tweetText.append(i.full_text)
#     tweetLikes.append(i.favorite_count)
#     time.append(i.created_at)

# df = pd.DataFrame({'Tweet Text': tweetText,'Likes': tweetLikes,'Time': time})

# df.to_csv('CNN.csv')

# df.to_csv('FoxNews.csv')

# df.to_csv('BBCWorld.csv')

# df.to_csv('SkyNews.csv')

# * part 2 (just comment the upper cursor and uncomment the below code and run)

# * api search for covid 

# cursor = api.search_tweets(q="covid",lang="en",count=numberOfTweets,tweet_mode="extended")

# for i in cursor:
#     tweetText.append(i.full_text)
#     tweetLikes.append(i.favorite_count)
#     time.append(i.created_at)
#     # print(i)

# df = pd.DataFrame({'Tweet Text': tweetText,'Likes': tweetLikes,'Time': time})

# df.to_csv('covidNews.csv')

channelName = ['@CNN','@FoxNews','@BBCWorld','@SkyNews']

def getTwitData(ID,numberOfTweets):
    tweetText = []
    tweetLikes = []
    time = []

    if(ID > 4):
        return

    cursor = tweepy.Cursor(api.user_timeline,id=f'{channelName[ID]}',tweet_mode="extended").items(numberOfTweets)

    for i in cursor:
        tweetText.append(i.full_text)
        tweetLikes.append(i.favorite_count)
        time.append(i.created_at)

    df = pd.DataFrame({'Tweet Text': tweetText,'Likes': tweetLikes,'Time': time})

    return df


if __name__ == '__main__':

    dfCNN = getTwitData(0,100)

    dfCNN.to_csv('CNN.csv')

    dfFoxNews = getTwitData(1,100)

    dfFoxNews.to_csv('FoxNews.csv')

    dfBCCNews = getTwitData(2,100)

    dfBCCNews.to_csv('BBCWorld.csv')

    dfSkyNews = getTwitData(3,100)

    dfSkyNews.to_csv('SkyNews.csv')

    print("DONE!")