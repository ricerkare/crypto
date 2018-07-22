from homebrewed_functions import *
from Crypto.Cipher import AES

b64encrypted_file2 = open("7.txt").read()
ciphertext = base64.b64decode(b64encrypted_file2)
Key2 = "YELLOW SUBMARINE"
cipher = AES.new(Key2, AES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext)

print(plaintext.decode())
