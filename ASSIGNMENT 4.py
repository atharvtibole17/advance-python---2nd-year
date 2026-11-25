#FIBONACCI USING MEMOIZATION:

def fibonacci(n, memo):
    if n == 0:

        return 0
    if n == 1:
        return 1
    
    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

n = int(input("ENTER n:"))
memo = {}
result = fibonacci(n,memo)
print("FIBONACCI NUMBER:",result)
print(memo)


# OUTPUT
ENTER n: 7
FIBONACCI NUMBER: 13
{2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13}
