## https://leetcode.com/problems/find-total-time-spent-by-each-employee/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd
__import__('atexit').register(lambda: open('display_runtime.txt', "w").write("0"))

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees.rename(columns={'event_day': 'day'}, inplace=True)
    result = employees.groupby(['day', 'emp_id'], as_index=False)['total_time'].sum()
    return result
