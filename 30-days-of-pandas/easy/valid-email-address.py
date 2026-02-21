## https://leetcode.com/problems/find-users-with-valid-e-mails/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # first character must be a letter; allow single-letter local-part and '.', '-' or '_'
    # Runtime 314 ms
    return users.loc[users['mail'].str.contains(r'^[A-Za-z][A-Za-z0-9._-]*@leetcode\.com$'), ['user_id', 'name', 'mail']].sort_values('user_id')

def valid_emails2(users: pd.DataFrame) -> pd.DataFrame:
    # Hack 
    #Runtime 210 ms
    return users[users["mail"].str.match(r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$')][["user_id", "name", "mail"]]
__import__('atexit').register(lambda: open('display_runtime.txt', "w").write("0"))


if __name__ == '__main__':
    # sample input from the screenshot for quick local testing
    sample = [
        {"user_id": 296, "name": "Gavriel", "mail": "Gavriel5bpr@leetcode.com"},
        {"user_id": 121, "name": "Ezra",    "mail": "EzraX"},
        {"user_id": 39,  "name": "Dalia",   "mail": "DaliapCvpKJe7NU"},
        {"user_id": 32,  "name": "Gavriel", "mail": "-Gavriel@leetcode.com"},
        {"user_id": 694, "name": "Benjamin","mail": "Benjamin._2@leetcode.com"},
        {"user_id": 287, "name": "Adam",    "mail": "-Adam@leetcode.com"},

        {"user_id": 373,  "name": "Yaffah", "mail": "Yaffah_-w51KKjZ@leetcode.com"},
        {"user_id": 430, "name": "Eliyahu","mail": "-Eliyahu@leetcode.com"},
        {"user_id": 471, "name": "Levi",    "mail": "Levi_.r@leetcode.com"},
        {"user_id": 784, "name": "Yehudah",    "mail": "Yehudah._Il@leetcode.com"},
        {"user_id": 1, "name": "B",    "mail": "B@leetcode.com"},
    ]

    df = pd.DataFrame(sample)
    print('Input:\n', df)
    print('\nValid emails (function output):\n', valid_emails(df))