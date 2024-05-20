#!/usr/bin/env python3
# h101_decrypt.py
import binascii

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

data = ("A4nEuSRBiqMVqAzfKPap2n0CJ8eL5J8D3uymb-diUhMzGqRqQ4HiRd-"
        "vZKF5665hJU7Gfy08WeNyCZ8ViA2M0w4eC8jkFRRvHs1lpuKs2hcXJ!"
        "cIn4Ety2tBjQjggQCFS5BVF9154P0fpfdPdCmn7IBsp!YGVpii5bjXJ"
        "CpS9uygVcY48JqoSnm-CnzbTB624!vhXkSEcjPGWH9NVcpNBQ~~")


def correct_data(incorrect_data: str):
    return incorrect_data.replace("~", "=").replace("-", "+").replace("!", "/")


corrected_data = correct_data(data)
print(f"Corrected data: {corrected_data}")

decoded_data = binascii.a2b_base64(corrected_data)
print(f"Decoded data: {decoded_data}")

# Extract IV (first 16 chars of string)

iv = decoded_data[:16]
cipher_text = decoded_data[16:]

print(f"IV: {iv}")
print(f"Cipher text: {cipher_text}")

# Placeholder for the key (actual length of placeholder 16 bytes)
key = b"sexteenbytekey!!"

# Create AES cypher and decrypt the cypher text
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_data = unpad(cipher.decrypt(cipher_text), AES.block_size)

print(f"Decrypted data: {decrypted_data.decode('utf-8')}")
