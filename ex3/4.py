def find_fibonacci_number(fi):
    a, b = 0, 1

    while b <= fi:
        a, b = b, a + b

    return b

result = find_fibonacci_number(10)
print(result)  # 13