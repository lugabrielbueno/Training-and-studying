#Given a non-empty string like "Code" return a string like "CCoCodCode".

#string_splosion('Code') → 'CCoCodCode'
#string_splosion('abc') → 'aababc'
#string_splosion('ab') → 'aab'


def string_splosion(string):
    answer = ''
    for i in range(len(string)):
        answer += string[:i]
    return answer+string

print(string_splosion('dufsuidfh'))
print(string_splosion('Gabriel'))