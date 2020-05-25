#Write a Python program to count the number 4 in a given list

def count_four(lis):
    try:
        answer = lis.count(4)
    except:
        print("WHOOPS! That's not a number")
    else:
        return answer
print(count_four([1,2,3,4,5,6]))
print(count_four([4,2,4,3,4,5,4,6]))