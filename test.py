def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def fibonacci_sequence(n):
    sequence = []
    for i in range(n):
        sequence.append(fibonacci(i))
    return sequence

def is_prime(number):
    if not isinstance(number, int) or number < 2:
        raise ValueError("Input must be an integer greater than 1")
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True