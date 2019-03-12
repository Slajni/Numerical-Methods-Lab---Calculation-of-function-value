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
    """Evaluates function value in standard way"""
    valToReturn = 0
    for key, value in coefs.items():
        valToReturn += val**key * value
    return valToReturn

def hornerEvaluation(coefit,val, checker=False):
    """Evaluates function value using horners alogirthm or checks if general condition is satisfied"""
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
    interval = [None,None]
    jumper = start
    while(hornerEvaluation(coefs,jumper,checker=True)==False):
        jumper += step
    interval[1] = jumper
    jumper = start
    coefficients = coefs.copy()
    if(len(coefficients)%2 - 1 == 1):
        for coeffitient in coefficients.values():
            coeffitient *= -1
    for key in coefficients.keys():
        if(key %2 == 1):
            coefficients[key] *= -1 # TODO: check the version with locals
    while(hornerEvaluation(coefficients,jumper,checker=True)==False):
        jumper += step
    interval[0] = jumper
    return interval


coefs = {0:-1,1:-3,2:1,3:-2,4:1}
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
#
