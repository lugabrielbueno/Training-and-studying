#Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

#xyz_there('abcxyz') → True
#xyz_there('abc.xyz') → False
#xyz_there('xyz.abc') → True
'''
def xyz_there(string):
    return 'xyz' in string

    str.endswith()
'''
x = 'abc.xyzxyz'

a = 'xyz' in x and x.endswith('xyz')
print(a)