from scipy import integrate as itg
import math


def fact(n: int) -> int:
    """Computes the factorial of a natural number.

    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    if n < 0:
        raise ValueError("n must be positive")
    if n == 0:
        return 1

    res = 1
    for i in range(1, n+1):
        res *= i
    return res


def roots(a: int, b: int, c: int) -> tuple:
    """Computes the roots of the ax^2 + bx + c = 0 polynomial.

    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
            to the roots of the ax^2 + bx + c polynomial.
    """
    delta = b**2 - 4*a*c
    if delta < 0:
        return tuple()
    if delta == 0:
        return (-b/2/a,)
    return ((-b - math.sqrt(delta))/2/a, (-b + math.sqrt(delta))/2/a)


def integrate(function, lower: float, upper: float) -> float:
    """Approximates the integral of a fonction between two bounds

    Pre: 'function' is a valid Python expression with x as a variable,
            'lower' <= 'upper',
            'function' continuous and integrable between 'lower' and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
            of the specified 'function'.

    Hint: You can use the 'integrate' function of the module 'scipy' and
            you'll probably need the 'eval' function to evaluate the function
            to integrate given as a string.
    """
    return itg.quad(lambda x: eval(function), lower, upper)[0]


if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', -1, 1))
