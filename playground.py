def factorial(a: int) -> int:
    if a == 1: return 1
    if a == 2: return 2
    return a * factorial(a - 1)

