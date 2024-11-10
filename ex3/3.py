def count_chars(s):
    uppercase_count = 0
    lowercase_count = 0
    other_count = 0

    for c in s:
        if c.isupper():
            uppercase_count += 1
        elif c.islower():
            lowercase_count += 1
        else:
            other_count += 1

    return (uppercase_count, lowercase_count, other_count)

result = count_chars("Hello, World! 123")
print(result) 