#Define a function which can generate a dictionary where the keys are numbers given (both included) and the values are square of keys. The function should just print the keys only.

def  sq_dic(a,b):
    dic = {}
    for num in range(a,b):
        key = num
        value = num**2
        dic[key] = value
    print(dic.keys())
