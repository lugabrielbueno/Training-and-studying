#Write a Python program to check whether a file exists

def check_exist(file):
    try:
        with open(file) as fl:
            fl.close()
    except FileNotFoundError:
        return False
    else:
        return True

print(check_exist('alarm.mp3'))
print(check_exist('phys.txt'))
print(check_exist('mydocs.txt'))
print(check_exist('music.mp3'))