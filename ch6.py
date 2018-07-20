def hamming_dist(S, T): # between byte strings S, T
    return sum(["{0:b}".format(S[i] ^ T[i]).count('1') for i in range(len(S))])

# The following returns a list of lists; for each list, the first element is keysize and the second element is the sum of hamming distances between blocks 1 and 2, between 2 and 3, et cetera, each of length keysize, then normalized.

def normalized_hamming_dists(input_string, keysize_max): 
    L = [[i, 0] for i in range(2, keysize_max+1)]
    for keysize in range(2, keysize_max + 1):
        for i in range(keysize):
            limit = len(input_string) // keysize - 1
            L[keysize-2][1] = sum([hamming_dist(input_string[keysize*j : keysize*(j+1)], input_string[keysize*(j+1) : keysize*(j+2)]) for j in range(limit)])
    return L

def break_repeating_key_xor(ciphertext, keysize):
    blocks = [ciphertext[i : i + keysize] for i in range(0, len(ciphertext),keysize)]
    transposed_blocks = "".join(list(itertools.zip_longest(*blocks, fillvalue = '\x00')))
    keychars = [break_single_char_xor(x.encode("utf-8"), "char_freqs") for x in transposed_blocks]
    return "".join(keychars)

b64encrypted_file1 = open("6.txt").read()
ct1 = base64.b64decode(b64encrypted_file1)
ksize = min(normalized_hamming_dists(ct1, 40), key=lambda x: x[1])[0]
Key1 = break_repeating_key_xor(ct1, ksize)
print(Key1)

