## https://leetcode.com/problems/customers-who-never-order/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return customers[~customers['id'].isin(orders['customerId'])][['name']].rename(columns={'name': 'Customers'})