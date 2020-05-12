# Calculate the amount Upper and lower case letters

string  = input()

ind = 0
cases = {'UPPER':0, 'lower':0}

while ind < len(string):
    if string[ind].islower():
        cases['lower'] += 1
    elif string[ind].isupper():
        cases['UPPER'] += 1
    ind += 1

print('UPPER ', cases['UPPER'])
print('lower ', cases['lower'])