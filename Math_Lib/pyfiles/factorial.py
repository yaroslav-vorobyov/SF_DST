def factorial(x):
    ans = 1

    if x < 0:
        raise ValueError('x must be greater than 0')

    for i in range(1, x+1):
        ans *= i

    return ans