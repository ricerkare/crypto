from homebrewed_functions import *

b64encrypted_file1 = open("6.txt").read()
ct1 = base64.b64decode(b64encrypted_file1)
ksize = min(normalized_hamming_dists(ct1, 40), key=lambda x: x[1])[0]
Key1 = break_repeating_key_xor(ct1, ksize)
print(Key1)

