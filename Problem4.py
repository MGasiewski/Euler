def is_palindrome(num):
    num_str = str(num)
    while len(num_str) > 0:
        if len(num_str) == 1:
            return True
        elif num_str[0] == num_str[len(num_str)-1]:
            num_str = num_str[1:len(num_str) - 1]
        else:
            return False
    return True


palindromes = []
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        product = i*j
        if is_palindrome(product):
            palindromes.append(product)

print(max(palindromes))