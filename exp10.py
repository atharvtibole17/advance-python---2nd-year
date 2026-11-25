#numpy
import numpy as np

# 1. Create an array from 1 to 10
arr = np.arange(1, 11)
print("Original Array:", arr)

# 2. Slicing operations
print("First five elements:", arr[:5])
print("Elements from index 3 to 7:", arr[3:8])
print("Alternate elements:", arr[::2])
print("Reversed Array:", arr[::-1])

# 3. Statistical measures
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# 4. Broadcasting
print("Add 5:", arr + 5)
print("Multiply by 2:", arr * 2)

# OUTPUT
Original Array: [ 1  2  3  4  5  6  7  8  9 10]
First five elements: [1 2 3 4 5]
Elements from index 3 to 7: [4 5 6 7 8]
Alternate elements: [1 3 5 7 9]
Reversed Array: [10  9  8  7  6  5  4  3  2  1]
Sum: 55
Mean: 5.5
Maximum: 10
Minimum: 1
Add 5: [ 6  7  8  9 10 11 12 13 14 15]
Multiply by 2: [ 2  4  6  8 10 12 14 16 18 20]
