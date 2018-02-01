r = 2
found = False
final_answer = []

while not found:
    for i in range(1, r):
        r_squared_by_two = (r**2)/2
        if r_squared_by_two % i == 0:
            s = r_squared_by_two / i
            t = r_squared_by_two / s
            triple = (r+s, r+t, r+s+t)
            if sum(triple) == 1000:
                final_answer = triple
                found = True
    r += 2

print(reduce(lambda x, y: x*y, final_answer, 1))