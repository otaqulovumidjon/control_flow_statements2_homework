def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    if number==int(number) and number>=1 and number<=7:
        if number==1:
            return "Monday"
        elif number==2:
            return "Tuesday"
        if number==3:
            return "Wednesday"
        elif number==4:
            return "Thursday"
        if number==5:
            return "Friday"
        elif number==6:
            return "Saturday"
        if number==7:
            return "Sunday"

print(main(15))