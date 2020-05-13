# Show amount in a bank account based on the operations

amount_account = 0
while True:
    s = input().split(" ")
    
    if not s:
        break
    

    operation = s[0]
    amount = int(s[1])

    if operation == 'D':
        amount_account += amount
    elif operation == 'W':
        amount_account -= amount

print(amount_account)