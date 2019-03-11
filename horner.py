def getCoefficients():
    """Returns a dictionary with coefficients"""
    coeffDict = {}
    num = 0
    coeffGot = input("Give me the value of the coefficient next to x{} or write quit to leave: ".format(num))
    while coeffGot !='quit':
        try:
            val = int(coeffGot)
            coeffDict[num] = val
            num += 1
        except ValueError:
            print("This is not a valid input")
        
        coeffGot = input("Give me the value of the coefficient next to x{} or write quit to leave: ".format(num))


    return coeffDict
    
