## https://leetcode.com/problems/invalid-tweets/submissions/1908166780/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    
    ## Runtime 342 ms
    ## return tweets.loc[ (tweets['content'].str.len() > 15 ), ['tweet_id']]

    ## Runtime 273 ms
    return tweets.loc[tweets['content'].apply(len) > 15, ['tweet_id']]