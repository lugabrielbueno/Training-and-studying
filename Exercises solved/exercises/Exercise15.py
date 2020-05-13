# Sum the digit repeating some times: 9 -> 9+99+999+9999

a = input()

# Concatenating the numbers as string before sum
aa = a+a
aaa = a+a+a
aaaa = a+a+a+a

# Sum
answer = int(a)+int(aa)+int(aaa)+int(aaaa)

print(answer)