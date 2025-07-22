x=2
n=-5
def power(x, n):
    if n == 0:
        return 1
    elif n<0:
        return (1/n)*power(x, n)
    else:
        return x * power(x, n - 1)
print(power(x, n)) 
        