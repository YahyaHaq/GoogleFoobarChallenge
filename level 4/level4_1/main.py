from __future__ import generators
import fractions
from collections import defaultdict
import math




def infinite_game_check(num1,num2):
    '''
    takes in number of bananas of player 1 and player2.
    returns True if game goes on infinetely otherwise returns False
    this is the brute force apporach. this has not been optimized yet
    '''
    banana_combinations = set()
    a = "a"
    change = 0
    iterations = 0
    while True:
        if num1 == num2:
            #game will end between both players as they have same number of bananas
            # print(change)
            return False
        #check if combination of bananas is already made or not
        if (num1,num2) in banana_combinations or (num2,num1) in banana_combinations:
            #game will go on infinitely
            return True
        else:
            banana_combinations.add((num1,num2))
            if num1>num2:
                num1 = num1 - num2
                num2 = num2 * 2
            else:
                #num2 > num1
                num2 = num2 - num1
                num1 = num1 * 2
        iterations+=1


def Log2(x):
    if x == 0:
        return False;
    return (math.log10(x) /
            math.log10(2))


# Function to check
# if x is power of 2
def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) ==
            math.floor(Log2(n)))

def infinite_game_check_optimized(num1,num2):
    gcd = fractions.gcd(num1,num2)
    sum = num1 + num2
    x = (sum/2)/gcd
    check = isPowerOfTwo(x)
    if check:
        return False
    else:
        return True


def solution(list):
    arr_size = len(list)
    ans = set()
    visited = [False] * arr_size
    degree = [0] * arr_size
    adjacency_list = {}
    for i in range(0, arr_size):
        for j in range(i + 1, arr_size):
            value = infinite_game_check_optimized(list[i], list[j])
            if value:
                degree[i] = degree[i] + 1
                degree[j] = degree[j] + 1
                ans.add((i, j))
                if i not in adjacency_list:
                    adjacency_list[i] = []
                if j not in adjacency_list:
                    adjacency_list[j] = []
                adjacency_list[i].append(j)
                adjacency_list[j].append(i)

    #NOW WE HAVE THIS INFORMATION:
    # - SET OF EDGES REPRESENTED IN AN ADJACENCY LIST
    # - LIST OF DEGREE OF EVERY NODE INDEXED BY NODE NUMBER
    # - LIST OF VISITED NODES INDEXED BY NODE NUMBER
    # print(adjacency_list)
    # print(degree)
    # print(visited)

    value = matching(adjacency_list)
    for node,matched_node in value.items():
        visited[node] = True
        visited[matched_node] = True
    count = 0
    for val in visited:
        if not val:
            count+=1
    return count

    #WHAT WILL WE DO WITH THIS INFORMATION:
    # - USE BLOSSOMS ALGORITHM TO FIND OPTIMAL MATCHING







def main():
    # # list = [1,7,1,1]
    # list = [1, 7, 3, 21, 13, 19]
    # output = solution(list)
    # print(output)
    j = 1073741823
    for i in range(1,10):
        value1 = infinite_game_check_optimized(i,j)
        value2 = infinite_game_check(i,j)
        if value1 == value2:
            continue
        else:
            print("WRONNGG")
            print(i,j)
            print("my value is ",value1)
            print("true value is ",value2)











if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
