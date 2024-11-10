def count_chars(string):
    upper_count = 0
    lower_count = 0
    digit_count = 0
    other_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            other_count += 1

    return (upper_count, lower_count, digit_count, other_count)

if __name__=='__main__':
    str1=input("请输入字符串：")
    print(count_chars(str1))