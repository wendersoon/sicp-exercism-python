import random

def remainder_square_checked(x, m):
    if (x != 1) and (x != m - 1) and ((x * x) % m == 1):
        return 0
    return (x * x) % m


def expmod_checked(base, exp, m):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return remainder_square_checked(expmod_checked(base, exp // 2, m), m)
    else:
        return (base * expmod_checked(base, exp - 1, m)) % m


def miller_rabin_test(n):
    a = random.randrange(1, n)
    return expmod_checked(a, n - 1, n) == 1


def miller_rabin_prime(n, times=10):
    if n < 2:
        return False
    for _ in range(times):
        if not miller_rabin_test(n):
            return False
    return True


def assert_result(test_name, actual, expected):
    status = "pass" if actual == expected else "fail"
    print(f"{status}: {test_name}")


# --- Testes equivalentes aos do Scheme ---
assert_result("   2 is prime",      miller_rabin_prime(2, 10), True)
assert_result("1009 is prime",      miller_rabin_prime(1009, 10), True)
assert_result("   4 is not prime",  miller_rabin_prime(4, 10), False)
assert_result("  99 is not prime",  miller_rabin_prime(99, 10), False)
assert_result(" 561 is not prime",  miller_rabin_prime(561, 10), False)  # 561 is Carmichael
