from textblob import TextBlob
import csv
import tweepy
import unidecode

# AUTHENTICATION (OAuth)

f = open('/Users/Marku/Documents/data_center/WorkSpace/Social-Media-Data-Analytics/Week4/auth.k','r')
ak = f.readlines()
f.close()
auth1 = tweepy.auth.OAuthHandler(ak[0].replace("\n",""), ak[1].replace("\n",""))
auth1.set_access_token(ak[2].replace("\n",""), ak[3].replace("\n",""))
api = tweepy.API(auth1)

# Tweeter search with keyword
target_num = 100
query = "trump"

csvFile = open('/Users/Marku/Documents/data_center/WorkSpace/Social-Media-Data-Analytics/Week4/results_trump.csv','w')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["username","author id","created", "text", "retwc", "hashtag", "followers", "friends","polarity","subjectivity"])
counter = 0

for tweet in tweepy.Cursor(api.search, q = query, lang = "en", result_type = "mixed", count = target_num  ).items():
    created = tweet.created_at
    text = tweet.text
    text = unidecode.unidecode(text) 
    retwc = tweet.retweet_count
    try:
        hashtag = tweet.entities[u'hashtags'][0][u'text'] #hashtags used
    except:
        hashtag = "None"
    username  = tweet.author.name            #author/user name
    authorid  = tweet.author.id              #author/user ID#
    followers = tweet.author.followers_count #number of author/user followers (inlink)
    friends = tweet.author.friends_count     #number of author/user friends (outlink)

    text_blob = TextBlob(text)
    polarity = text_blob.polarity
    subjectivity = text_blob.subjectivity
    
    t = text_blob.detect_language
    print(t)
    
    csvWriter.writerow([str(username).encode("utf-8"), authorid, created, str(text).encode("utf-8"), retwc, hashtag, followers, friends, polarity, subjectivity])

    counter = counter + 1
    if (counter == target_num):
        break

csvFile.close()

