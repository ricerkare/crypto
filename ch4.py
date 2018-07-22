import binascii, os, base64
os.chdir(os.path.expanduser('~') + '/src/crypto')
from homebrewed_functions import *

os.chdir(os.path.expanduser("~") + "/src/crypto")
hexes = open("4.txt").read().split('\n')
hexes = [binascii.unhexlify(x) for x in hexes]

H = hexes[0]

Key0 = max([break_single_char_xor(x, method="dictionary", show_metric=True) for x in hexes], key=lambda x: x[1])
print(Key0)

Key0 = ''
maxwc = 0
