#検索ワードに引っかかった投稿にいいねを投稿する。
#フォロー機能は鬱陶しいので外す

import tweepy
#secret_key にアカウントのシークレット情報などが記されている
import sys
sys.path.append('..')
import part_1
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

#指定した条件（検索ワード、検索件数) に一致するユーザ情報を取得

#取得したユーザーを1件ずついいね、フォローしていく
def auto_good():
    #part_1で作った検索システムを利用して自動いいね機能を実装する
    search_results = part_1.search()
    #print(secret_key)
    for result in search_results:
        status_id = result.id 
        status_text = result.text 
        user_name = result.user.name 
        user_id = result.user.id 

        # good 
        try : 
            api.create_favorite(status_id)
            print("Liked Status : " + status_text)

        except Exception as e :
            print(e)
    
def auto_follow():
    #part_1で作った検索システムを利用して自動フォロー機能を実装する

    search_results = part_1.search()
    #print(secret_key)
    for result in search_results:
        status_id = result.id 
        status_text = result.text 
        user_name = result.user.name 
        user_id = result.user.id 

        # good 

        try: 
            api.create_friendship(user_id)
            print("Followed : " + user_name + "(@" + str(user_id) + ")")
        
        except Exception as e :
            print(e)

if __name__ == "__main__" :
    pass 
    #auto_good()
    auto_follow()
