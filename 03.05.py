import string
text = input("Enter a string:")
words = text.split()
result = ""
for word in words:
    clean_word = ""
    for char in word:
        if char not in string.punctuation:
            clean_word += char
    if clean_word:
         result += clean_word.capitalize()
hashtag = "#" + result
hachtag = hashtag[:140]
print(hachtag)