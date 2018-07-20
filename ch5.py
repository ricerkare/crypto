def repeating_xor(msg, key): # for byte strings msg and key
    return "".join([chr(msg[i] ^ key[i%len(key)]) for i in range(len(msg))]).encode("utf-8", "replace")

string3 = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal".encode("utf-8", "replace")
enc = repeating_xor(string3, "ICE".encode("utf-8", "replace"))
dec = repeating_xor(enc, "ICE".encode("utf-8", "replace"))

print(binascii.hexlify(enc))
print(dec)
