def knapsack(wt, profit, gain, n, product, capacity):
    for i in range (n):
       #0/1 part
        if(wt[i] <= capacity):
            product[i] = 1
            gain += profit[i]
            capacity -= wt[i]
        
         #fractional part
        else:
            frac = capacity / wt[i]
            capacity = 0
            gain += profit[i] * frac
            product[i] = frac
    return gain, product

# Example usage
wt = [10, 20, 30]
profit = [60, 100, 120]
n = len(wt)
capacity = 50
ratio = [profit[i] / wt[i] for i in range(n)]
items = sorted(zip(ratio, wt, profit), reverse=True)
wt = [item[1] for item in items]
profit = [item[2] for item in items]
product = [0] * n
gain = 0
result, product = knapsack(wt, profit, gain, n, product, capacity)
print("Maximum profit:", result)
print("Items included:", product)
