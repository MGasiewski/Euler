mults_of_three_or_five = [x for x in range(1000) if x % 3 == 0 or x % 5 == 0]
sum_of_both = sum(mults_of_three_or_five)
print(sum_of_both)
