#!/usr/bin/env python3


__author__      = "ADD YOUR NAME!!!"
__date__        = "16 Oct 2019"

def printLine():
    print("\t","-" * 50)
#end of printLine()

def fibsList(n):
    """The Fibonacci Sequence to be used for comparison to your own sequence"""
    # stavely's chapter 7
    result_list = [ ]
    a=1
    b=1

    for i in range(n):
        result_list.append(a)
        a, b = b, a + b
    return result_list
# end of FibList()



def fibByArm(m, gRatio_flt):
# The function to compute the fibonacci sequence based on the golden ratio
# Note, m is a previous term, and gRatio_flt is the Golden Ratio (Phi)
    printLine()
#   TODO: calculate your fibonacci sequence using the arm mesaurements (phi)

#end of fibByArm()





def main():
    print(" Welcome to the Fibonacci Sequence calculator using the Golden")
    print(" Ratio which has been prepared from measurments of your arm. ")
    printLine()
    iterations_int = 15
    print(" The Real Fibonacci Sequence for",iterations_int,"iterations:")
    print(fibsList(iterations_int))
# get user input (As floats) for both measurements
#    sf_flt = float(input(" Length of shoulder tip of longest finger : "))
#    ef_flt = float(input(" Length of elbow to tip of longest finger : "))

#   TODO: add code to work with these measurments and call the fibByArm() function

#end of main()



# this is used for the math.ciel() function that rounds up values to nearest integer
import math
if __name__ == "__main__":
	main()
