#Write a Python program to concatenate all elements in a list into a string and return it

def concat_list(lis):
    string = ' '.join(lis)
    return string.strip()

lista = 'hello world, i am learning python'.split()
lista2 = 'enjoy the movie'.split()

print(concat_list(lista))
print(concat_list(lista2))