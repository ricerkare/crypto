import binascii, os, base64
os.chdir(os.path.expanduser('~') + '/src/crypto')
from ch3 import *

char_freqs = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182 
}


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
                    
os.chdir(os.path.expanduser("~") + "/src/crypto")
hexes = open("4.txt").read().split('\n')
hexes = [binascii.unhexlify(x) for x in hexes]

Key0 = max([break_single_char_xor(x, method="char_freqs", show_metric=True) for x in hexes], key=lambda x: x[1])
print(Key0)

Key0 = ''
maxwc = 0
