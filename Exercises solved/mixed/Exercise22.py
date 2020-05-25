# Counting the words in a phrase or text

text = input().split()
counted = {}

# Checking the string word by word
for word in text:
    counting = {word: str(text.count(word))}
    
    # Updating the dict with new word frequency
    counted.update(counting)

# Final count
for coun in counted.items():
    print(':'.join(coun))
    