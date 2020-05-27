#Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

#count_code('aaacodebbb') → 1
#count_code('codexxcode') → 2
#count_code('cozexxcope') → 2

def count_code(string):
    count = 0
    for index,letter in enumerate(string):
        try:
            if letter =='c' and string[index+1] == 'o' and string[index +3] == 'e':
                count +=1
        except IndexError:
            continue
    return count

print(count_code('cozexxcope'))