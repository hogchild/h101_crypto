#!/usr/bin/env python3
# h101_decrypt.py

import click

from .h101_decryptor import Aes128Decryptor


@click.command(
    help="This app will decrypt any text, provided a 16-char encryption key."
)
@click.option(
    "-k", "--encryption-key", "encryption_key",
    help="The encryption key you want to decrypt with.",
    required=True,
    prompt="Type the encryption key you would like to decrypt with",
    default="sixteenbytekey!!",
    type=str,
)
@click.option(
    "-d", "--data-to-decrypt", "data_to_decrypt",
    help="The string of data you want to encrypt (no b'' characters).",
    required=True,
    prompt="Type the string of data you would like to decrypt",
    default=b'eCuu+sQfXBkvPHwChvtL2KRzwc4h+7SodYFOmxrRzxw=',
    type=str,
)
def main(encryption_key, data_to_decrypt):
    encryptor = Aes128Decryptor(encryption_key, data_to_decrypt)
    encryptor.decrypt()


if __name__ == "__main__":
    main()
