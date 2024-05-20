#!/usr/bin/env python3
# h101_decryptor.py

import binascii

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from rich.console import Console


class Aes128Decryptor:
    """
    Decrypts an AES 128-bit encrypted string.
    """

    def __init__(self, encryption_key: str, data: bytes):
        """
        The encryption key needs to be the exact 16-char long string
        used originally to encrypt the data.
        :param encryption_key: Original 16-byte passphrase used for encryption.
        :param data: The string of data which needs to be decrypted.
        """
        self.c = Console()
        self.encryption_key = encryption_key.encode("utf-8")
        self.data_to_decrypt = data
        self.base64_decoded_data = b""
        self.iv = b""
        self.iv_stripped_data = b""
        self.decrypted_data = b""
        self.unpadded_data = b""

    def base64_decode_data(self):
        self.base64_decoded_data = binascii.a2b_base64(self.data_to_decrypt)

    def extract_iv(self):
        self.iv = self.base64_decoded_data[:16]

    def iv_strip_data(self):
        self.iv_stripped_data = self.base64_decoded_data[16:]

    def aes128_decrypt_data(self):
        cipher = AES.new(self.encryption_key, AES.MODE_CBC, self.iv)
        self.decrypted_data = cipher.decrypt(self.iv_stripped_data)

    def unpad_data(self):
        self.unpadded_data = unpad(self.decrypted_data, 16)

    def decrypt(self):
        self.base64_decode_data()
        self.c.print(f"[+] Base64 decoded AES 128 encrypted data: {self.base64_decoded_data}", style="bright_red")
        self.extract_iv()
        self.c.print(f"[+] IV: {self.iv}", style="green_yellow")
        self.iv_strip_data()
        self.c.print(f"[+] IV-stripped base64 decoded AES 128 encrypted data: {self.iv_stripped_data}",
                     style="cyan3")
        self.aes128_decrypt_data()
        self.c.print(f"[+] AES 128 decrypted data: {self.decrypted_data}", style="dark_cyan")
        self.unpad_data()
        self.c.print(f"[+] Unpadded data: {self.unpadded_data}", style="green4")


def main():
    data_to_decrypt = b'eCuu+sQfXBkvPHwChvtL2KRzwc4h+7SodYFOmxrRzxw='
    encryptor = Aes128Encryptor("sixteenbytekey!!", data_to_decrypt)
    encryptor.decrypt()


if __name__ == "__main__":
    main()
