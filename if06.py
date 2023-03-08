def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    n1 = n%10
    n//=10
    n2 = n%10
    n//=10
    n3 = n%10
    n//=10
    n4 = n%10
    n//=10
    n5 = n%10

    if n1>=n2 and n1>=n3 and n1>=n4 and n1>=n5:
        return 1
    if n2>=n1 and n2>=n3 and n2>=n4 and n2>=n5:
        return 2
    if n3>=n1 and n3>=n2 and n3>=n4 and n3>=n5:
        return 3
    if n4>=n1 and n4>=n1 and n4>=n1 and n4>=n5:
        return 4
    if n5>=n1 and n5>=n2 and n5>=n3 and n5>=n4:
        return 5

print(main(87394))