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
    if a==int(a) and a<b and a<c:
        return 'a kichik'
    if b==int(b) and b<a and b<c:
        return 'b kichik'
    if c==int(c) and c<a and c<b:
        return 'c kichik'

print(main(21.3,31,41))