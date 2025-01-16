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

    def primes_in_range(a, b):
        if not (isinstance(a, int) and isinstance(b, int)):
            raise ValueError("Both inputs must be integers")
        if a == b:
            raise ValueError("The interval cannot be of zero length")
        
        start, end = min(a, b), max(a, b)
        primes = [num for num in range(start, end + 1) if is_prime(num)]
        return primes

        def split_into_threes(text):
            if not isinstance(text, str):
                raise ValueError("Input must be a string")
            if len(text) % 3 != 0:
                raise ValueError("The length of the text must be a multiple of three")
            return [text[i:i+3] for i in range(0, len(text), 3)]
        
        def caesar_encode(text, shift):
            if not isinstance(text, str):
                raise ValueError("Input must be a string")
            if not isinstance(shift, int):
                raise ValueError("Shift must be an integer")

            def shift_char(c):
                if 'a' <= c <= 'z':
                    return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
                elif 'A' <= c <= 'Z':
                    return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
                elif c in ' .':
                    return c
                else:
                    raise ValueError("Invalid character in text")

            encoded_text = ''.join(shift_char(c) for c in text)
            if any(c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .'
                   for c in encoded_text):
                raise ValueError("Encoded text contains invalid characters")
            return encoded_text

        def caesar_decode(encoded_text, shift):
            return caesar_encode(encoded_text, -shift)