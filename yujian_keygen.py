# cdoing:utf-8
# Author: Akkuman

# pip install pycryptodome

from Crypto.Cipher import AES
import sys

def crypt_code(machine_code):
    key = bytes([15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15])
    cipher = AES.new(key, AES.MODE_ECB)
    data = str.encode(machine_code)
    while len(data) % 16 != 0:
        data += b'\0'
    return cipher.encrypt(data).hex().upper()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python the.py yourMachineCode")
    else:
        print(crypt_code(sys.argv[1]))