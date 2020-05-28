#Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().

#no_teen_sum(1, 2, 3) → 6
#no_teen_sum(2, 13, 1) → 3
#no_teen_sum(2, 1, 14) → 3

def fix_teen(n):
    teen = [x for x in range(13,20) if x!=15 and x!=16]
    if n not in teen:
        return n
    else:
        return 0
def no_teen_sum(a,b,c):
    return 0 + fix_teen(a) + fix_teen(b) + fix_teen(c)


'''
def no_teen_sum(a,b,c):
    
    summ = 0
    if a in teen and b in teen and c in teen:
        summ += 0
    elif a in teen and b in teen:
        summ += c
    elif a in teen and c in teen:
        summ += b
    elif b in teen and c in teen:
        summ += a
    elif a in teen:
        summ += b+c
    elif b in teen:
        summ += a+c
    elif c in teen:
        summ += a+b
    elif (a,b,c) not in teen:
        summ += a+b+c
    return summ
    '''