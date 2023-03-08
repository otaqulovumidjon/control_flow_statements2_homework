def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """ 
    if a>b and a>c:
        return "a katta"
    elif b>c and b>a:
        return "b katta"
    if c>a and c>b:
        return "c katta"

print(main(31, 41, 51))