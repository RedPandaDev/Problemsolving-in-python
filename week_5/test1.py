def doomsday(y):
    
    """
    >>> doomsday(2012)
    3
    >>> doomsday(1899)
    2
    >>> doomsday(1923)
    3
    >>> doomsday(10000)
    -1
    >>> doomsday(1756)
    -1
    >>> type(doomsday(2010))
    <class 'int'>
    """
    x = 0
    w = 0
    day = 0

    #Set x depending on the year
    if (y < 1900 and y >= 1800):
        x = 5
        # Minus the year so we know the year of the century
        w = y - 1800

    elif (y < 2000 and y >= 1900):
        x = 3
        w = y - 1900

    elif (y < 2100 and y >= 2000):
        x = 2
        w = y - 2000

    elif (y < 2200 and y >= 2100):
        x = 0
        w = y - 2100

    elif (y < 1800 or y >= 2200):
        day = -1


    #Divide w by 12 and call the quotient a and the remainder b
    a = w // 12
    b = w % 12

    #Divide b by 4 and call the quotient c
    c = b // 4

    #Divide the sum of a, b and c by 7 and call the remainder d
    d = (a + b + c) % 7

    #Count forward d days from x to get the year's doomsday
    if day != -1:
        day = x + d
        if day > 6:
            # minus 7 as there is 0 for 7 days
            day -= 7
    return day
