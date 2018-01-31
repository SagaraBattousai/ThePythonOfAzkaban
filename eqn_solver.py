import numpy as np
from numpy import linalg as LA
import sys
import re

def getFromUserInput():

    polynomial_size = int(input("-----> Please Enter Polynomial Size: "))
    
    needed_equ = polynomial_size + 1

    print("Need " + str(needed_equ) + " param, value pairs")

    equ_range = range(needed_equ)

    X = []
    Y = []

    for i in equ_range:
        X.append(float(input("-----> Please Enter A Parameter: ")))
        Y.append(float(input("-----> Please Enter a Value: ")))

    return equ_range, X, Y

def getFromList(args):

    polynomial_size = args[0]
    
    needed_equ = int(polynomial_size) + 1

    equ_range = range(needed_equ)

    X = []
    Y = []

    Xregex = "(?<=\().*(?=,)"
    Yregex = "(?<=,).*(?=\))"

    for i in args[1:]:
        X.append(float(re.search(Xregex, i).group(0)))
        Y.append(float(re.search(Yregex, i).group(0)))


    return equ_range, X, Y


if __name__ == "__main__":


    if len(sys.argv) < 2:
        equ_range, X, Y = getFromUserInput()
    else:
        equ_range, X, Y = getFromList(sys.argv[1:])



    equ = np.power(np.array(X).reshape(-1, 1), list(reversed(equ_range)))

    answer = np.dot(LA.inv(equ), np.array(Y).reshape(-1,1))

    print(answer)


