#Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

#end_other('Hiabc', 'abc') → True
#end_other('AbC', 'HiaBc') → True
#end_other('abc', 'abXabc') → True

def end_other(a,b):
    a = a.lower()
    b = b.lower()
    return a.endswith(b) or b.endswith(a)
'''
def end_other(a,b):
    a,b = a.lower(),b.lower()
    ab,ba = len(a)-len(b),len(b) -len(a)
    finda,findb = b.find(a), a.find(b)
    if finda == -1 and findb == -1:
      return False
    return a.find(b) == ab or b.find(a) == ba
'''