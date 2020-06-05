#Write a Python program to solve (x + y) * (x + y)

def solution(x,y):
    return '('+str(x)+'+'+str(y)+') ^ 2 = '+ str((x+y)**2)

print(solution(4,6))
print(solution(10,10))
print(solution(2,1))