def getCoefficients():
    """Returns a dictionary with coefficients"""
    coeffDict = {}
    num = 0
    coeffGot = input("Give me the value of the coefficient next to x^{} or write quit to leave: ".format(num))
    while coeffGot !='quit':
        try:
            val = int(coeffGot)
            coeffDict[num] = val
            num += 1
        except ValueError:
            print("This is not a valid input")
        
        coeffGot = input("Give me the value of the coefficient next to x^{} or write quit to leave: ".format(num))


    return coeffDict
    



valueOfX = 10   # hardcoded value of x in polynomial


def normalEvaluation(coefs,val):
    """Evaluates function value in standard way"""
    valToReturn = 0
    for key, value in coefs.items():
        valToReturn += val**key * value
    return valToReturn

print(normalEvaluation(getCoefficients(),valueOfX))


