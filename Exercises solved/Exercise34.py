#Pig Latin - Pig Latin is a game of alterations played on the English language game. To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.

st = input('Give me a word : ')

cons = 'bcdfghjklmnpqrstvwxyz'
vowel = 'aeiou'


if (st[0] in cons) and (st[1] in cons):
    #if two initial letter are both consonant
    first = st[0]
    sec = st[1]
    st =st.replace(st[0],' ')
    st = st.replace(st[1],' ')
    st = st.strip()
    print((st+first+sec+'ay').title())

elif st[0] in cons:
    #if the initial letter is a consonant
    first = st[0]
    st = st.replace(st[0],' ')
    st = st.strip()
    print((st+first+'ay').title())

elif st[0] in vowel:
    #if the initial letter is a vowel
    print(st+'ay')