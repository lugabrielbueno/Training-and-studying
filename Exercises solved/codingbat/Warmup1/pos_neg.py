#Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.

#pos_neg(1, -1, False) → True
#pos_neg(-1, 1, False) → True
#pos_neg(-4, -5, True) → True

def pos_neg(a,b,negative):
    if negative:
        return a<0>b
    elif not negative :
        return a>0>b or a<0<b


print(pos_neg(-4, 5, True))