# h101_crypto

This app is made up of two basic tools to encrypt text using AES 128-bit encryption.
h101_encrypt is for encrypting, h101_decrypt for decrypting.

```commandline
Usage: python -m h101_crypto.h101_encrypt [OPTIONS]

  This app will encrypt any text, provided a 16-char encryption key.

Options:
  -k, --encryption-key TEXT   The encryption key you want to encrypt with.
                              [required]
  -d, --data-to-encrypt TEXT  The string of data you want to encrypt.
                              [required]
  --help                      Show this message and exit.
```

```commandline
Usage: python -m h101_crypto.h101_decrypt [OPTIONS]

  This app will decrypt any text, provided a 16-char encryption key.

Options:
  -k, --encryption-key TEXT   The encryption key you want to decrypt with.
                              [required]
  -d, --data-to-decrypt TEXT  The string of data you want to encrypt (no b''
                              characters).  [required]
  --help                      Show this message and exit.
```