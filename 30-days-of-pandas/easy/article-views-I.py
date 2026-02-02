## https://leetcode.com/problems/article-views-i/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    #Solution 1 - Runtime 354ms
    result = views[views['author_id'] == views['viewer_id']][['author_id']].rename(columns={'author_id': 'id'})
    result = result.drop_duplicates().sort_values(by='id').reset_index(drop=True)
    return result

    ##Solution 2 - Runtime 287 ms
    author_ids = views[views['author_id'] == views['viewer_id']]['author_id'].unique()
    return pd.DataFrame({'id': sorted(author_ids)})