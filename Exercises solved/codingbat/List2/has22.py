#Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

#has22([1, 2, 2]) → True
#has22([1, 2, 1, 2]) → False
#has22([2, 1, 2]) → False

def has22(lis):
    answer = False
    for i,x in enumerate(lis):
        if x == 2 and (i != len(lis)-1) and lis[i+1] == 2:
            answer = True
    return answer