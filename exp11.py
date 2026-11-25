import pandas as pd
import numpy as np

# 1. Create a Series of 10 random numbers
s = pd.Series(np.random.randint(1, 100, 10))
print("Original Series:")
print(s)

# 2. Indexing
print("\nFirst element:", s[0])
print("First five elements:")
print(s[:5])

# 3. Filtering
print("\nNumbers greater than 50:")
print(s[s > 50])

# 4. Statistical operations
print("\nMean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())

# OUTPUT
Original Series:
0    45
1    78
2    12
3    65
4    34
5    91
6    23
7    56
8    88
9    10
dtype: int64

First element: 45
First five elements:
0    45
1    78
2    12
3    65
4    34
dtype: int64

Numbers greater than 50:
1    78
3    65
5    91
7    56
8    88
dtype: int64

Mean: 50.2
Median: 50.5
Minimum: 10
Maximum: 91
