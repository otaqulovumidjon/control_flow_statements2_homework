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
    if a>b:
        return "a katta"
    elif b>c:
        return "b katta"
    else:
        return "c katta"

print(main(31, 41, 51))