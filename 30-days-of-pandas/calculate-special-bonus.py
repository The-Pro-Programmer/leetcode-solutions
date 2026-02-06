## https://leetcode.com/problems/calculate-special-bonus/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    ## Runtime 329ms
    employees['bonus'] = ((employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith('M'))) * employees['salary']
    return employees[['employee_id', 'bonus']].sort_values("employee_id")