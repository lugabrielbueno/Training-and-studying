# Numbers between 1000 and 3000 that all digits is even number

answer = []

for numbers in range(1000,3001):
    numbers = str(numbers)
    
    i = 0
    candidate = 0
    while i <= 3:
        
        each_one = int(numbers[i])
        if each_one % 2 == 0:
            candidate += 1
            i += 1
            if candidate == 4:
                answer.append(numbers)
        else:
            i += 1
print(','.join(answer))

#VERY BAD CODE HERE