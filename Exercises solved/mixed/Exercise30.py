#prime number counter

limit = int(input('From zero to: '))
prim = {x for x in range(1,limit+1)}
no_prime = set()

for number in prim:
    counter = 0
    for num in range(1,limit+1):
        if number% num ==0:
            counter +=1
    if counter != 2:
        no_prime.add(number)
prim = prim - no_prime
prim = list(prim)
prim.sort()
print(prim)
print("Between 1 and {}, there's {} prime numbers.".format(limit,len(prim)) )