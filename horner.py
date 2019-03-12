import time 
def getCoefficients():
    """Returns a dictionary with coefficients"""
    coeffDict = {}
    num = 0
    coeffGot = input("Give me the value of the coefficient next to x^{} or write quit to leave: ".format(num))
    while coeffGot !='quit':
        try:
            val = float(coeffGot)
            coeffDict[num] = val
            num += 1
        except ValueError:
            print("This is not a valid input")
        
        coeffGot = input("Give me the value of the coefficient next to x^{} or write quit to leave: ".format(num))


    return coeffDict
    
def normalEvaluation(coefs,val):
    """Evaluates function value in standard way
    
    
    Keyword arguments:
    coefs -- dictionary with coefficients and their values
    val -- value of a parameter for which function is gonna be evaluated
    
    """
    valToReturn = 0
    for key, value in coefs.items():
        valToReturn += val**key * value
    return valToReturn

def hornerEvaluation(coefit,val, checker=False):
    """Evaluates function value using horners alogirthm or checks if general condition is satisfied
    
    
    Keyword arguments:
    coefits -- dictionary with coefficients and their values
    val -- value of a parameter for which function is gonna be evaluated
    checker -- false by default, if true function instead of the function value returns the logical value informing if the general condition is satisfied
    
    """
    satisfies = True
    coefs = coefit.copy()
    hValue = coefs[len(coefs)-1]
    del coefs[len(coefs)-1]
    for i in range(len(coefs)-1,-1,-1):
        hValue = hValue*val + coefs[i]
        if hValue < 0 and checker == True:
            satisfies = False
            break
    if(checker):
        return satisfies
    else:
        return hValue

def findBoundsOfRoots(coefs,step=0.1,start=0.1):
    """returns the interval in which roots of polynomial are included
    
    if evaluation of alorithm takes too long it is assumed that polynomial is unbounded on one or both sides


    Keyword arguments:
    coefs -- dictionary with coefficients and their names
    step -- the rate in which we change value of evaluation to search for bounds
    start -- starting value for searching

    """
    
    interval = [None,None]
    jumper = start
    timer = time.time()
    while(hornerEvaluation(coefs,jumper,checker=True)==False):
        jumper += step
        if float(time.time() - timer) > 10:
            interval[1] = float("inf")
    if interval[1] == None:
        interval[1] = jumper
    jumper = start
    coefficients = coefs.copy()
    if((len(coefficients)-1)%2 == 1):
        for coeffitient in coefficients.values():
            coeffitient *= -1
    for key in coefficients.keys():
        if(key %2 == 1):
            coefficients[key] *= -1 # TODO: check the version with locals
    while(hornerEvaluation(coefficients,jumper,checker=True)==False):
        jumper += step
        if float(time.time() - timer) > 10:
            interval[0] = float("inf")
    if interval[0] == None:
        interval[0] = jumper
    return interval


coefs = {0:1,1:0,2:1}
#coefs = getCoefficients()
valueOfX = 10   # hardcoded value of x in polynomial
times = 1 #how many times you want to perform alorithm?

timePassed = time.time()
result = None

for i in range(0,times):
    result = normalEvaluation(coefs, valueOfX)
timePassed= time.time() - timePassed
print(timePassed)
result = None
timePassed = time.time()
for i in range(0,times):
    result = hornerEvaluation(coefs,valueOfX)
timePassed = time.time() - timePassed
print(timePassed)

print(findBoundsOfRoots(coefs))
print(hornerEvaluation(coefs,10))
#

