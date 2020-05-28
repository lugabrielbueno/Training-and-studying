#Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

#xyz_there('abcxyz') → True
#xyz_there('abc.xyz') → False
#xyz_there('xyz.abc') → True

def xyz_there(string):
    find_xyz = string.find('xyz')
    find_dot = string.find('.')
    if find_dot == -1:
        return 'xyz' in string
    else:
        return find_xyz -1 != find_dot