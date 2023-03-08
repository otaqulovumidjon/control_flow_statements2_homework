def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    n1 = n % 10
    n //= 10
    n2 = n % 10
    n //= 10
    n3 = n % 10
    n //= 10
    n4 = n % 10
    n //= 10
    n5 = n % 10
    max = n1
    if n2 > max:
        max = n2
    if n3 > max:
        max = n3
    if n4 > max:
        max = n4
    if n5 > max:
        max = n5
    return max

print(main(89349)) 