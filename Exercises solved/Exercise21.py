# Calculating the distances that robot walk

# Lets creating a list to refer the movement
movement = []

#Receiving the steps
while True:
    steps = input()
    if not steps:
        break
    movement.append(tuple(steps.split(' ')))

# Creating list to coordinates
x_y = [0,0]

#Checking the relative positions
for position,coordinat in movement:
    if position == 'UP':
        x_y[1] += int(coordinat)
    elif position == 'DOWN':
        x_y[1] -= int(coordinat)
    elif position == 'LEFT':
        x_y[0] -= int(coordinat)
    elif position == 'RIGHT':
        x_y[0] += int(coordinat)

#Calculating the final distance
answer = sum(x_y)
print(answer)