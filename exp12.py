import numpy as np
import pandas as pd

# Create customer dataset
data = {
    'CustomerID': [101, 102, 103, 104, 105, 106],
    'Age': [25, 35, 45, np.nan, 30, 50],
    'MonthlyCharges': [500, 700, 900, 600, np.nan, 800],
    'Tenure': [2, 12, 24, 6, 3, 36],
    'Churn': ['Yes', 'No', 'No', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['MonthlyCharges'] = df['MonthlyCharges'].fillna(
    df['MonthlyCharges'].mean()
)

print("\nCleaned Data:")
print(df)

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Churn count
print("\nChurn Count:")
print(df['Churn'].value_counts())

# Average charges by churn
print("\nAverage Monthly Charges:")
print(df.groupby('Churn')['MonthlyCharges'].mean())

# OUTPUT
Original Data:
   CustomerID   Age  MonthlyCharges  Tenure Churn
0         101  25.0           500.0       2   Yes
1         102  35.0           700.0      12    No
2         103  45.0           900.0      24    No
3         104   NaN           600.0       6   Yes
4         105  30.0             NaN       3   Yes
5         106  50.0           800.0      36    No

Cleaned Data:
   CustomerID   Age  MonthlyCharges  Tenure Churn
0         101  25.0           500.0       2   Yes
1         102  35.0           700.0      12    No
2         103  45.0           900.0      24    No
3         104  37.0           600.0       6   Yes
4         105  30.0           700.0       3   Yes
5         106  50.0           800.0      36    No

Summary Statistics:
       CustomerID        Age  MonthlyCharges     Tenure
count    6.000000   6.000000        6.000000   6.000000
mean   103.500000  37.000000      700.000000  13.833333
std      1.870829   9.273618      141.421356  13.541295
min    101.000000  25.000000      500.000000   2.000000
25%    102.250000  31.250000      625.000000   3.750000
50%    103.500000  36.000000      700.000000   9.000000
75%    104.750000  43.000000      775.000000  21.000000
max    106.000000  50.000000      900.000000  36.000000

Churn Count:
Churn
Yes    3
No     3
Name: count, dtype: int64

Average Monthly Charges:
Churn
No     800.0
Yes    600.0
Name: MonthlyCharges, dtype: float64

Average Tenure:
Churn
No     24.000000
Yes     3.666667
Name: Tenure, dtype: float64

# Compare average tenure
print("\nAverage Tenure:")
print(df.groupby('Churn')['Tenure'].mean())
