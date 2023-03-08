def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    n1 = n//10000
    n2 = n//1000%10
    n3 = n//100%10
    n4 = n//10%10
    n5 = n%10
    if n1>=n2 and n1>=n3 and n1>=n4 and n1>=n5:
        return n1

    if n2>=n1 and n2>=n3 and n2>=n4 and n2>=n5:
        return n2

    if n3>=n1 and n3>=n2 and n3>=n4 and n3>=n5:
        return n3

    if n4>=n1 and n4>=n2 and n4>=n3 and n4>=n5:
        return n4

    if n5>=n1 and n5>=n2 and n5>=n3 and n5>=n4:
        return n5

print(main(89349))