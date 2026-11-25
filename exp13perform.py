import threading
import time

# Task 1: Count numbers
def count_numbers():
    for i in range(1, 6):
        print("Count:", i)
        time.sleep(1)

# Task 2: Check even numbers
def check_even():
    for i in range(1, 6):
        if i % 2 == 0:
            print(i, "is Even")
        time.sleep(1)

# Task 3: Check odd numbers
def check_odd():
    for i in range(1, 6):
        if i % 2 != 0:
            print(i, "is Odd")
        time.sleep(1)

# Main function
def main():
    t1 = threading.Thread(target=count_numbers)
    t2 = threading.Thread(target=check_even)
    t3 = threading.Thread(target=check_odd)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    # OUTPUT
    Count: 1
1 is Odd
Count: 2
2 is Even
1 is Odd
Count: 3
Count: 4
3 is Odd
4 is Even
Count: 5
5 is Odd
All tasks completed.

    print("All tasks completed.")

main()
