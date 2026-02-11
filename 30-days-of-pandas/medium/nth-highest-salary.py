## https://leetcode.com/problems/nth-highest-salary/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    """Return a DataFrame with the Nth highest unique salary.

    If there is no Nth highest salary, returns a DataFrame with None.
    """
    # handle missing/empty salary column
    if 'salary' not in employee.columns or employee['salary'].dropna().empty:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})

    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)

    if N > len(unique_salaries) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    else:
        return pd.DataFrame({f'getNthHighestSalary({N})': [unique_salaries.iloc[N - 1]]})


if __name__ == '__main__':
    # Example 1
    emp1 = pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})
    print('Example 1 input:')
    print(emp1)
    print('\nExample 1 output:')
    print(nth_highest_salary(emp1, 2))

    print('\n' + '-' * 40 + '\n')

    # Example 2
    emp2 = pd.DataFrame({'id': [1], 'salary': [100]})
    print('Example 2 input:')
    print(emp2)
    print('\nExample 2 output:')
    print(nth_highest_salary(emp2, 2))