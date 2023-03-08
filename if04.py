def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    if a>b:
        x = "a katta"
    if b>a:
        x = "b katta"
    if a==b:
        x = 0
    return x
print(main(85, 85))