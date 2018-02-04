"""

   myUtil.py

"""

def isPrime(inputNum):

    # num is integer & Natural Number ?
    num = int(inputNum)
    if ((num<=0) | (num != inputNum)):
        raise ValueError("{0} is not Natural Number.".format(inputNum))

    # check num is prime
    if (num == 1):
        return False
    else:
        i = 2
        # To Effective Calc, Use num/2.
        while ( i <= num/2):
            if ( num%i == 0):
                return False
            else:
                i += 1
        return True
