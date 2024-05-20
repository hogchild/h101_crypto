#!/usr/bin/env python3
# h101_encrypt.py

from .h101_encryptor import Aes128Encryptor

import click


@click.command(
    help="This app will encrypt any text, provided a 16-char encryption key."
)
@click.option(
    "-k", "--encryption-key", "encryption_key",
    help="The encryption key you want to encrypt with.",
    required=True,
    prompt="Type the encryption key you would like to encrypt with",
    default="sixteenbytekey!!",
    type=str,
)
@click.option(
    "-d", "--data-to-encrypt", "data_to_encrypt",
    help="The string of data you want to encrypt.",
    required=True,
    prompt="Type the string of data you would like to encrypt",
    default= "Hello snake!",
    type=str,
)
def main(encryption_key, data_to_encrypt):
    encryptor = Aes128Encryptor(encryption_key, data_to_encrypt)
    encryptor.encrypt()


if __name__ == "__main__":
    main()
