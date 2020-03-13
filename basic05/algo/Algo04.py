def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i -= 1

def gcd2(a, b):
    print("gcd:", a, b)
    if b == 0:
        return a
    return gcd2(b, a % b)

def fibonacci(n):
    print(n-2, n-1)
    if n <= 1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(6))


