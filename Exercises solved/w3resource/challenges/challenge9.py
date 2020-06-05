#Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit.

def rep_int(num):
    answer = None
    for digit in str(num):
        if len(str(answer)) != 1:
            answer = 0
            answer += int(digit)
    return answer

print(rep_int(59))
print(rep_int(100))