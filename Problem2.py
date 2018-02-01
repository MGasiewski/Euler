term1 = 1
term2 = 2
even_fibs = set()
even_fibs.add(term2)

while term2 < 4000000:
    temp = term1 + term2
    if temp % 2 == 0:
        even_fibs.add(temp)
    term1 = term2
    term2 = temp

print(sum(even_fibs))
