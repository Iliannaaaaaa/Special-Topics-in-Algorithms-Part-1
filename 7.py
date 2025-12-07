def fibonacci_fast_doubling(n):
    # Base case
    if n == 0:
        return 0, 1

    # Get F(k) and F(k+1) where k = n // 2
    f_k, f_k_plus_1 = fibonacci_fast_doubling(n // 2)

    # F(2k) = F(k) * (2*F(k+1) - F(k))
    f_2k = f_k * (2 * f_k_plus_1 - f_k)

    # F(2k+1) = F(k+1)^2 + F(k)^2
    f_2k_plus_1 = f_k_plus_1**2 + f_k**2

    if n % 2 == 0:
        return f_2k, f_2k_plus_1
    else:
        return f_2k_plus_1, f_2k + f_2k_plus_1

if __name__ == "__main__":
    n = int(input("Enter n: "))
    result, _ = fibonacci_fast_doubling(n)
    print(f"F({n}) = {result}")