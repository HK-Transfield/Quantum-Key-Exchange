#!/usr/bin/env python3
# ---------------------------------------------------------------------------
__author__ = "HK Transfield"
# ---------------------------------------------------------------------------
""" A simple encryption algorithm using Exclusive-OR (XOR) logic."""
# ---------------------------------------------------------------------------


def cipher(message: list, key: list) -> list:
    """Encrypts a message using XOR logic.

    This function can be used to both encypt and decrypt a 
    ciphered message, provided the same key is used both ways.

    Parameters
    ----------
    message : list 
        The plain message that will be encrypted
    key : list 
        Used to apply a XOR mask over a message

    Returns
    ----------
    list 
        The final ciphered message
    
    Raises
    ----------
    ZeroDivisionError
        There is no key passed in, resulting in there
        being a modulo division with zero
    """

    ciphered_message = []

    try:
        for i in range(len(message)):

            # Modulo division to repeat key if shorter than message
            j = i % len(key)

            # Perform XOR bitwise operator
            xor = message[i] ^ key[j]
            ciphered_message.append(xor)

        return ciphered_message

    except ZeroDivisionError:
        print("Error: Cannot encrypt with an empty key!")
