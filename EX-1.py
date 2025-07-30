from string import punctuation,ascii_lowercase,ascii_uppercase,digits, whitespace
from random import shuffle

original = list(punctuation + ascii_lowercase + ascii_uppercase + digits + whitespace)
encrypted = original.copy()
shuffle(encrypted)
encrypted_word=""
while True:
    word = input("Enter a text to encrypt: ")
    for i in word:
        idx = original.index(i)
        encrypted_word += encrypted[idx]

    print(f"The encrypted word is : {encrypted_word}")
    














