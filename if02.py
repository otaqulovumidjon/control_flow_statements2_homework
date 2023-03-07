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
    if a==int(a) and b==int(b) and a<b:
        if a==int(a) and c==int(c) and a<c:
            x = 'a kichik'
        else:
            x = 'c kichik'
    else:
        if b==int(b) and c==int(c) and b<c:
            x = 'b kichik'
        else:
            x = 'c kichik'
    return x

print(main(21,31,4))