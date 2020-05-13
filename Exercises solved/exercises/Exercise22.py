# Counting the words in a phrase or text

text = input().split()
counted = {}
for word in text:
    counting = {word: str(text.count(word))}
    counted.update(counting)
for coun in counted.items():
    print(':'.join(coun))
    