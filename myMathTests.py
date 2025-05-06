
#Paulo Juarez
# April 21, 2025




from myMath import ( add, subtract, multiply, divide, power, factorial, is_prime, sum_of_digits, gcd, fib, lcm, square_root, abs_diff, log, mod, mean, median, mode, celsius_to_fahrenheit, fahrenheit_to_celsius, inverse, triangular_number)

import pytest

def test_add():
    assert add(1, 2) == 3
    
def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(6, 2) == 3
    try:
        divide(1, 0)
        assert False
    except ZeroDivisionError:
        assert True

def test_power():
    assert power(2, 3) == 8

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    try:
        factorial(-1)
        assert False
    except ValueError:
        assert True

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(4) is False
    assert is_prime(17) is True
    assert is_prime(1) is False

def test_sum_of_digits():
    assert sum_of_digits(123) == 6

def test_gcd():
    assert gcd(48, 18) == 6

def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(5) == 5

def test_lcm():
    assert lcm(4, 6) == 12

def test_square_root():
    assert square_root(9) == 3

def test_abs_diff():
    assert abs_diff(5, 3) == 2

def test_log():
    import math
    assert log(100, 10) == math.log(100, 10)
    try:
        log(0)
        assert False
    except ValueError:
        assert True

def test_mod():
    assert mod(10, 3) == 1

def test_mean():
    assert mean([1, 2, 3]) == 2

def test_median():
    assert median([1, 2, 3]) == 2
    assert median([1, 2, 3, 4]) == 2.5

def test_mode():
    assert mode([1, 2, 2, 3]) == 2

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 254

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 80

def test_inverse():
    assert inverse(2) == 0.5
    try:
        inverse(0)
        assert False
    except ZeroDivisionError:
        assert True

def test_triangular_number():
    assert triangular_number(5) == 15


# Guardamos este archivo como myMathTests.py
#with open("/mnt/data/myMathTests.py", "w") as f:
 #   f.write(test_code
#"/mnt/data/myMathTests.py" 
