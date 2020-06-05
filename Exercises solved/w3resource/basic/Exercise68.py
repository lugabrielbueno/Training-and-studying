#Write a Python program to calculate the sum of the digits in an integer

def sum_digits(n):
    answer = 0
    n = abs(n)
    for x in str(n):
        answer += int(x)
    return answer

print(sum_digits(1234))
print(sum_digits(-943))