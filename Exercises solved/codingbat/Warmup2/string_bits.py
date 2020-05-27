#Given a string, return a new string made of every EVEN char starting with the first, so "Hello" yields "Hlo".

#string_bits('Hello') → 'Hlo'
#string_bits('Hi') → 'H'
#string_bits('Heeololeo') → 'Hello'

def string_bits(string):
    i = 0
    answer = ''
    while i != len(string):
        if i%2 == 0:
            answer += string[i]
        i +=1
    return answer