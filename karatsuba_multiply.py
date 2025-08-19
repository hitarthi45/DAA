def karatsuba(x, y):
    """Perform Karatsuba multiplication on two integers x and y."""
    if x < 10 or y < 10:
        return x * y
    m = max(len(str(x)), len(str(y)))
    if(m%2!=0):
        m -= 1
    a, b = divmod(x, 10**(m//2))
    c, d = divmod(y, 10**(m//2))
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    abcd = karatsuba(a + b, c + d)-ac-bd
    return ((ac * (10**m)) + (abcd * (10**(m//2))) + bd)

x = input("Enter first number: ")
y = input("Enter second number: ")
result = karatsuba(int(x), int(y))
print(result)