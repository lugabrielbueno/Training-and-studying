# Show the odd number in a given sequence

odd = [x for x in input().split(',') if int(x) % 2 != 0]

print(','.join(odd))