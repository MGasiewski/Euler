found = False
collatz_table = {}
highest = []

for i in range(1, 1000000):
    val = i
    current = []
    while True:
        if val == 1:
            current.append(val)
            collatz_table[i] = current
            if len(current) > len(highest):
                highest = current
            break
        elif val in collatz_table:
            current = current + collatz_table[val]
            collatz_table[i] = current
            if len(current) > len(highest):
                highest = current
            break
        elif val % 2 == 0:
            current.append(val)
            val = val // 2
        elif val % 2 == 1:
            current.append(val)
            val = val * 3 + 1

print(highest)