import os, binascii
os.chdir(os.path.expanduser('~') + "/src/crypto")
from ch2 import xor
words = open("words_alpha.txt").read().split('\n')

def single_char_xors(msg):
    for i in range(256):
        yield [chr(i).encode("utf-8"), xor(msg, (chr(i)*len(msg)).encode("utf-8"))]

def real_word_count(S): # Assumes there is at least one three-letter word in the string S. Doesn't look up contractions (yet).
    count = 0
    for word in filter(lambda s: s.isalpha() and len(s) >= 3, S.split(' ')):
        if word.lower() in words:
            count += 1
    return count

string2 = binascii.unhexlify("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
decoded2 = max(single_char_xors(string2), key=lambda s: real_word_count(s[1].decode("utf-8", "replace")))
print(string2.decode() + " xor " + decoded2[0].decode() + " is " + decoded2[1].decode())