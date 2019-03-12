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
    






def normalEvaluation(coefs,val):
    """Evaluates function value in standard way"""
    valToReturn = 0
    for key, value in coefs.items():
        valToReturn += val**key * value
    return valToReturn

def hornerEvaluation(coefit,val):
    """Evaluates function value using horners alogirthm"""
    coefs = coefit.copy()
    hValue = coefs[len(coefs)-1]
    del coefs[len(coefs)-1]
    for i in range(len(coefs)-1,-1,-1):
        hValue = hValue*val + coefs[i]
    return hValue


coefs = {0:7,1:3,2:2}
#coefs = getCoefficients()
valueOfX = 10   # hardcoded value of x in polynomial

print(normalEvaluation(coefs,valueOfX))
print(hornerEvaluation(coefs,valueOfX))


#
