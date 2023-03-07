def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a<b:
        if a<c:
            x = 'a kichik'
        else:
            x = 'c kichik'
    else:
        if b<c:
            x = 'b kichik'
        else:
            x = 'c kichik'
    return x

print(main(21,31,4))