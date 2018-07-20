# For byte strings S, T 
def xor(S, T): 
    return "".join([chr(s ^ t) for s, t in zip(S, T)]).encode("utf-8", "replace")

def single_char_xors(msg):
    for i in range(256):
        yield [chr(i).encode("utf-8"), xor(msg, (chr(i)*len(msg)).encode("utf-8"))]

# For byte strings msg, key
def repeating_xor(msg, key): 
    return "".join([chr(msg[i] ^ key[i%len(key)]) for i in range(len(msg))]).encode("utf-8", "replace")

# Assumes there is at least one three-letter word in the string S. Doesn't look up contractions (yet).
def real_word_count(S): 
    count = 0
    for word in filter(lambda s: s.isalpha() and len(s) >= 3, S.split(' ')):
        if word.lower() in words:
            count += 1
    return count

def freq_score(S):
    return sum([char_freqs[ch.lower()] for ch in S if ch in char_freqs])

def break_single_char_xor(ciphertext, method = "dictionary", show_metric = False): 
    if method == "dictionary":
        Key = ''
        max_word_count = 0
        for x in single_char_xors(ciphertext):
            if real_word_count(x[1].decode()) > max_word_count:
                max_word_count = real_word_count(x[1])
                Key = x[0]
        if show_metric:
            return [Key, max_word_count]
        else:
            return Key
    elif method == "char_freqs":
        Key = ''
        max_freq = 0.0
        for x in single_char_xors(ciphertext):
            if float(freq_score(x[1].decode("utf-8", "replace"))) > max_freq:
                max_freq = freq_score(x[1])
                Key = x[0]
        if show_metric:
            return [Key, max_freq]
        else:
            return Key

# Hamming distance between byte strings S, T:
def hamming_dist(S, T): 
    return sum(["{0:b}".format(S[i] ^ T[i]).count('1') for i in range(len(S))])

# Returns a list of lists; for each list, the first element is keysize and the second element is the sum of hamming distances between blocks 1 and 2, between 2 and 3, et cetera, each of length keysize, then normalized.

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
