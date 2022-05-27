from fractions import Fraction

'''
Gearing Up for Destruction
==========================

As Commander Lambda's personal assistant, you've been assigned the task of configuring the LAMBCHOP doomsday device's axial orientation gears. It should be pretty simple -- just add gears to create the appropriate rotation ratio. But the problem is, due to the layout of the LAMBCHOP and the complicated system of beams and pipes supporting it, the pegs that will support the gears are fixed in place.

The LAMBCHOP's engineers have given you lists identifying the placement of groups of pegs along various support beams. You need to place a gear on each peg (otherwise the gears will collide with unoccupied pegs). The engineers have plenty of gears in all different sizes stocked up, so you can choose gears of any size, from a radius of 1 on up. Your goal is to build a system where the last gear rotates at twice the rate (in revolutions per minute, or rpm) of the first gear, no matter the direction. Each gear (except the last) touches and turns the gear on the next peg to the right.

Given a list of distinct positive integers named pegs representing the location of each peg along the support beam, write a function solution(pegs) which, if there is a solution, returns a list of two positive integers a and b representing the numerator and denominator of the first gear's radius in its simplest form in order to achieve the goal above, such that radius = a/b. The ratio a/b should be greater than or equal to 1. Not all support configurations will necessarily be capable of creating the proper rotation ratio, so if the task is impossible, the function solution(pegs) should return the list [-1, -1].

For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12, the second gear could have a radius of 14, and the last one a radius of 6. Thus, the last gear would rotate twice as fast as the first one. In this case, pegs would be [4, 30, 50] and solution(pegs) should return [12, 1].

The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers, all between 1 and 10000 inclusive.
'''
from fractions import Fraction


def solution(array):
    ##TO DO###
    # find way to create standard form of outputs
    # test on input size of 4 and 5
    ##########
    if ((not array) or len(array) == 1):
        return [-1, -1]

    rhs_arr = []

    for i, val in enumerate(array):
        if i == len(array) - 1:
            rhs_arr.append(Fraction(0))
        else:
            rhs_arr.append(Fraction(array[i + 1] - val))
    size = len(rhs_arr)
    intial_value = rhs_arr[:size - 1]

    # subtract second last row from previous row till we reach the first row
    for i in range(size - 2, 0, -1):
        rhs_arr[i - 1] = rhs_arr[i - 1] - rhs_arr[i]

    # subtract last row from first row
    rhs_arr[size - 1] = Fraction(-1 * rhs_arr[size - 1]) + rhs_arr[0]
    if size % 2 == 0:
        rhs_arr[size - 1] = rhs_arr[size - 1] / Fraction(3.0)
    rhs_arr[:size - 1] = intial_value

    for i in range(size - 1, 0, -1):
        rhs_arr[i - 1] = rhs_arr[i - 1] - rhs_arr[i]

    # return rhs_arr
    for value in rhs_arr:
        if value <= 0:
            return [-1, -1]
    #
    #
    # value = float(rhs_arr[0])
    output = rhs_arr[0].limit_denominator(100000000000000000)

    if output < 2:
        return [-1, -1]

    for value in rhs_arr:
        if value >= 1:
            continue
        else:
            return [-1, -1]

    return [output.numerator, output.denominator]
