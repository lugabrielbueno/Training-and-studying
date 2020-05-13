# Calculate amount letters and numbers

# Receiving the data
string = input()

# Initializing counters
letters = 0
digits = 0
ind = 0

#Analising each digit and letter typed
while ind < len(string):
    if string[ind].isdigit() == True:
        digits += 1
    elif string[ind].isalpha() == True:
        letters += 1
    ind += 1

print('Letters = '+str(letters))
print('Digits = '+str(digits))