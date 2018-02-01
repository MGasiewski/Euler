from math import sqrt


def get_factors(num):
    root_of_num = int(sqrt(num))
    factors = []
    factors.append(1)
    factors.append(num)

    for i in range(2, root_of_num):
        if num % i == 0:
            factors.append(i)
            factors.append(num / i)

    return factors


factors = get_factors(600851475143)

factors.sort(reverse=True)
for factor in factors:
    if len(get_factors(factor)) == 2:
        print(factor)
        break
