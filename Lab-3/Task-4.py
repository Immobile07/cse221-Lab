def fast_exponentiation(a, b, mod):
    result = 1
    a = a % mod
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b = b // 2
    return result

def geometric_series_sum(a, n, m):
    if a == 1:
        return n % m
    mod = m * (a - 1)
    a_n = fast_exponentiation(a, n, mod)
    sum_series = (a * (a_n - 1)) // (a - 1)
    return sum_series % m

def main():
    T = int(input())
    for _ in range(T):
        a, n, m = map(int, input().split())
        print(geometric_series_sum(a, n, m))

if __name__ == "__main__":
    main()
