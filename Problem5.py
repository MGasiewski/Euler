num = 1
factors = [1]
for i in range(20, 1, -1):
    if i not in factors:
        num *= i

print(factors)