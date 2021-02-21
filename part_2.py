#どんなkey があるのか？

import tweepy
#secret_key にアカウントのシークレット情報などが記されている
import sys
sys.path.append('..')
from secret import  secret_key

sec = secret_key.Secret()

CONSUMER_KEY = sec.CONSUMER_KEY
CONSUMER_SECRET = sec.CONSUMER_SECRET
ACCESS_TOKEN = sec.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = sec.ACCESS_TOKEN_SECRET
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth ,wait_on_rate_limit = True)
Account = sec.Account #取得したいユーザーのユーザーIDを代入　@より後ろ


tweets = api.user_timeline(Account, count=20, page=1)

print(type(api.me()))
print(type(api.__dict__.keys()))

for i in tweets[0].__dict__.keys():
    print(i)
    #tweetのkeyをすべて表示している
print(tweets[0].text)#[n]最新記事からn番目　を取得できる

