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
        x="First number"
    elif b>c:
        x="Second number"
    else:
        x="Third number"
    return x

print(main(3, 41, 5))