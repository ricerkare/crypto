from homebrewed_functions import *

string3 = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal".encode("utf-8", "replace")
enc = repeating_xor(string3, "ICE".encode("utf-8", "replace"))
dec = repeating_xor(enc, "ICE".encode("utf-8", "replace"))

print(binascii.hexlify(enc))
print(dec)
