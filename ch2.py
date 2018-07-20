import binascii

string0 = binascii.unhexlify("1c0111001f010100061a024b53535009181c")
string1 = binascii.unhexlify("686974207468652062756c6c277320657965")

def xor(S, T): # assumes S, T are byte strings
    return "".join([chr(s ^ t) for s, t in zip(S, T)]).encode("utf-8", "replace")

print(string0, string1)
print(binascii.hexlify(xor(string0, string1)))
