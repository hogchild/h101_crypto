#!/usr/bin/env python3
# h101_encrypt.py

import binascii

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from rich.console import Console


class Aes128Encryptor:
    """
    Encrypts a string using AES 128-bit cryptography.
    """
    def __init__(self, encryption_key: str, data: str):
        """
        The encryption key can be any 16-char long string.
        :param encryption_key: 16 byte passphrase for encryption.
        :param data: The string of data which needs to be encrypted.
        """
        self.c = Console()
        self.encryption_key = encryption_key.encode("utf-8")
        self.data_to_encrypt = data.encode("utf-8")
        self.iv = b""
        self.padded_data = b""
        self.encrypted_data = b""
        self.base64_encoded_data = b""

    def generate_iv(self):
        self.iv = get_random_bytes(16)

    def pad_data(self):
        self.padded_data = pad(self.data_to_encrypt, 16)

    def aes128_encrypt_data(self):
        cipher = AES.new(self.encryption_key, AES.MODE_CBC, self.iv)
        self.encrypted_data = cipher.encrypt(self.padded_data)

    def base64_encode_data(self):
        combined_data = self.iv + self.encrypted_data
        self.base64_encoded_data = binascii.b2a_base64(combined_data).strip()

    def encrypt(self):
        self.generate_iv()
        self.c.print(f"[+] IV: {self.iv}", style="bright_red")
        self.pad_data()
        self.c.print(f"[+] Padded data: {self.padded_data}", style="green_yellow")
        self.aes128_encrypt_data()
        self.c.print(f"[+] AES 128 Encrypted data: {self.encrypted_data}", style="dark_cyan")
        self.base64_encode_data()
        self.c.print(f"[+] Base64 encoded AES 128 encrypted data: {self.base64_encoded_data}", style="green4")


def main():
    data_to_encrypt = "Hello snake!"
    encryptor = Aes128Encryptor("sixteenbytekey!!", data_to_encrypt)
    encryptor.encrypt()


if __name__ == "__main__":
    main()
