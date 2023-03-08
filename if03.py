def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """

    if b>a and a>c or c>a and a>b:
        x = 'First number'

    if a>b and b>c or c>b and b>a:
        x = 'Second number'
    
    if a>c and c>b or b>c and c>a:
        x = 'Third number'

    return x

print(main(2, 4, 6))