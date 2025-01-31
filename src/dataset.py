import time


def factorial_recursive(n):
    """Computes factorial recursively."""
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    """Computes factorial iteratively."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def compare_factorial_methods(n):
    """Compares execution times of recursive and iterative factorial calculations."""
    start = time.time()
    rec_result = factorial_recursive(n)
    rec_time = time.time() - start

    start = time.time()
    iter_result = factorial_iterative(n)
    iter_time = time.time() - start

    print(f"Factorial of {n}: {rec_result}")
    print(f"Recursive Time: {rec_time:.6f} sec")
    print(f"Iterative Time: {iter_time:.6f} sec")


# Test the function with a number
compare_factorial_methods(10)
