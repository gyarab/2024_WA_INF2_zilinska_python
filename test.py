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
 