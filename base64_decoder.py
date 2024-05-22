#!/usr/bin/env python3
# base64_decoder.py

import base64

obfuscated_strings = ['aiegpjhfljfnoleaadplpifglekgklpm', 'CMvZCg9UC2vuzxH0', 'ndG4swjuB2XQ', 'CNvUDgLTzq', 'ndeWm3zgs3Ptrq', 'r0vu',
                      'mtaZotC3oxL6qu5pDG', 'mtb5y1vIwKW', 'zxjYB3i', 'C2vUza', 'C2v0DgLUz3m',
                      'mJqXmZGWA0XSBxH3', 'mti5mdeZt3L1sK1N', 'CgfYC2u', 'mZiWotrorhbJrve',
                      'mZjLEfvlBgu', 'mtaZmZbkuuP5wvO', 'C2v0DgLUz3mUANnVBG', 'EwjbENy', 'oduZnte4ueHIsLjK',
                      'mZq0nJfOs2nWtMK', 'z2v0vvjm',
                      'ls0Gre9nieLUDMfKzxi6ienVDwXKig5VDcbSB2fKihnLDhrPBMDZlIbuCNKGzw5HyMXPBMCGDgHLihjLBw92'
                      'zsbWzxjTAxnZAw9UCYbWB2XPy3KGAgvHzgvYigLUihnLDhrPBMDZlG']


class Base64Unobfuscator:
    def __init__(self, base64_encoded_strings: list):
        self.obfuscated_strings = base64_encoded_strings
        self.word = ""

    def fix_missing_pad(self, word):
        missing_pad = 4 - (len(word) % 4)
        return word + "=" * missing_pad

    def unobfuscate(self, word):
        fixed_pad_word = self.fix_missing_pad(word)
        try:
            return base64.b64decode(fixed_pad_word).decode("utf-8")
        except UnicodeError:
            return base64.b64decode(fixed_pad_word).decode("latin-1")

    def process_obfuscated_strings(self):
        return [self.unobfuscate(self.word) for self.word in self.obfuscated_strings]


def main():
    unobfuscator = Base64Unobfuscator(obfuscated_strings)
    unobfuscated_strings = unobfuscator.process_obfuscated_strings()
    print(unobfuscated_strings)


if __name__ == "__main__":
    main()