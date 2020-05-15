#Define a function that can accept multiple strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.


def maxima(*args):
    answer = ''
    #loop for to verify every word
    for arg in args:

        #Condition to substitute
        if len(arg) > len(answer):
            answer = arg

        # Condition to concatenate
        elif len(arg) == len(answer):
            answer = answer+'\n'+arg
            
    print(answer)

