def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_sum(start, end):
    prime_list = []
    total = 0
    for num in range(start, end + 1):
        if is_prime(num):
            prime_list.append(num)
            total += num
    print(f"在[{start}, {end}]范围内的所有质数为：{prime_list}")
    return total

if __name__=="__main__":
    sum = prime_sum(1, 100)
    print(f"[1, 100]范围内质数的和为：{sum}")