## https://leetcode.com/problems/patients-with-a-condition/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

## Runtime 280 ms
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    def has_diab1(conditions):
        if not conditions or not isinstance(conditions, str):
            return False
        return any(code.startswith('DIAB1') for code in conditions.split())
    
    return patients.loc[patients['conditions'].apply(has_diab1), ['patient_id', 'patient_name', 'conditions']]



if __name__ == '__main__':
    # sample input from the attached image
    sample = [
        {"patient_id": 1, "patient_name": "Daniel", "conditions": "YFEV_COUGH"},
        {"patient_id": 2, "patient_name": "Alice", "conditions": ""},
        {"patient_id": 3, "patient_name": "Bob", "conditions": "DIAB100 MYOP"},
        {"patient_id": 4, "patient_name": "George", "conditions": "ACNE DIAB100"},
        {"patient_id": 5, "patient_name": "Alain", "conditions": "DIAB201"},
        {"patient_id": 6, "patient_name": "George", "conditions": "ACNE +DIAB100"},
    ]

    df = pd.DataFrame(sample)
    print("Input:\n", df)
    print("\nDiabetic patients (function output):\n", find_patients(df))