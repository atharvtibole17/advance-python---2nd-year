import threading
import time

# Task 1: Count numbers
def count_numbers():
    for i in range(2, 9):
        print("Count:", i)
        time.sleep(1)

# Task 2: Calculate squares
def calculate_squares():
    for i in range(2, 9):
        print("Square of", i, "=", i * i)
        time.sleep(1)

# Task 3: Calculate cubes
def calculate_cubes():
    for i in range(2, 9):
        print("Cube of", i, "=", i ** 3)
        time.sleep(1)

# Main function
def main():
    t1 = threading.Thread(target=count_numbers)
    t2 = threading.Thread(target=calculate_squares)
    t3 = threading.Thread(target=calculate_cubes)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("All tasks completed.")

main()

# OUTPUT 
Count: 2
Square of 2 = 4
Cube of 2 = 8
Count: 3
Square of 3 = 9
Cube of 3 = 27
Count: 4
Square of 4 = 16
Cube of 4 = 64
Count: 5
Square of 5 = 25
Cube of 5 = 125
Count: 6
Square of 6 = 36
Cube of 6 = 216
Count: 7
Square of 7 = 49
Cube of 7 = 343
Count: 8
Square of 8 = 64
Cube of 8 = 512
All tasks completed.
