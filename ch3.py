import binascii
from homebrewed_functions import *

string2 = binascii.unhexlify("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
decoded2 = max(single_char_xors(string2), key=lambda s: real_word_count(s[1].decode("utf-8", "replace")))
print(string2.decode() + " xor " + decoded2[0].decode() + " is " + decoded2[1].decode())
