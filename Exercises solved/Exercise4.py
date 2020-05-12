# Receive a sequence and add on a tuple and a list

# Catching and appending the sequence on the list
sequence = str(input('Type a sequence: '))

# Spliting the list on comma
seq_list = sequence.split(',')

# Attributing a tuple using the first list as reference
seq_tuple = tuple(seq_list)

print(seq_list)
print(seq_tuple)