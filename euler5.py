"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20
"""

from functools import partial


# It really works!!
def lcm(numbers):
    return reduce(lambda x, y: (x*y)/gcd(x,y), numbers, 1)

def small_divided_by_all(lim):
    divisors = [x for x in range(1, lim + 1)]
    solution = []

    for i in range(10000):
        result = True
        for d in divisors:
            result  = result and divisor(i, d)

        if result:
            solution.append(i)

        if len(solution) == 1:
            break

    return solution


def brainiac():
    import operator

    divisors = [x for x in range(1, lim + 1)]
    return reduce(operator.add, valores)

def divisor(num, factor):
    return num % factor == 0


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


