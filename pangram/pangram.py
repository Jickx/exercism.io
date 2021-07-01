import string

def is_pangram(sentence):
    alphabet = list(string.ascii_lowercase)
    for i in sentence.lower():
        if i in alphabet:
            alphabet.remove(i)
    if not alphabet:
        return True
    else:
        return False




