"""
tweet投稿方法
tweetのデータ取得方法
trend取得の方法など
"""

#

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

# user = api.get_user(screen_name = Account)
# print(user)

#tweets = api.user_timeline(Account, count=200, page=1) #アカウントのツイート取得
#tweets = api.home_timeline(count=10, page=1,result_type="recent")

def search():
    #特定のキーワードを検索する
    search_key = input() #検索ワード
    tweets = api.search(q='"{}"'.format(search_key), lang='ja', result_type='recent',count=5)

    num = 1 #ツイート数を計算するための変数
    for tweet in tweets:
        print('twid : ', tweet.id)               # tweetのID
        print('user : ', tweet.user.screen_name)  # ユーザー名
        print('date : ', tweet.created_at)      # 呟いた日時
        print(tweet.text)                  # ツイート内容
        print('favo : ', tweet.favorite_count)  # ツイートのいいね数
        print('retw : ', tweet.retweet_count)  # ツイートのリツイート数
        print('ツイート数 : ', num) # ツイート数
        print('='*80) # =を80個表示
        num += 1 # ツイート数を計算
    
    return tweets

def get_trend():
    #その地域のトレンドを取得する
    woeid = {
        "日本": 23424856,
        "札幌": 1118108, "仙台": 1118129, 
        "東京": 1118370, "京都": 15015372, "大阪": 15015370,
        "広島": 1117227, "福岡": 1117099, "沖縄": 2345896
    }

    woeid = {"沖縄": 2345896}
    trend_list = []

    for area, wid in woeid.items():
        print("--- {} ---".format(area))
        # リストになっているので取り出す
        trends = api.trends_place(wid)[0]
        #print(trends.keys()) # trends, as_of, created_at, locations
        #print(len(trends["trends"])) # 50

        
        for i, content in enumerate(trends["trends"]):

            print(i+1, content['name'])
            trend_list.append(str(i+1))
            trend_list.append(content['name'])
            trend_list.append("\n")
            if (i == 4):
                break

        print("----------")

        #print(" ".join(trend_list))

def tweet():
    #ツイートを投稿する
    sentence = input()
    api.update_status(sentence)



if __name__ == "__main__" :
    pass

    #search()
    # get_trend()
    # tweet()