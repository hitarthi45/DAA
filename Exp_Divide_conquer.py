x = int(input("Enter the base (x): "))
n = int(input("Enter the exponent (n): "))
def power(x, n):
    if n == 0:
        return 1
    temp = power(x, n//2)
    if n % 2 == 0:
        return temp * temp
    else:
        return temp * temp * x
print(power(x, n))