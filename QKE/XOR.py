# https://www.101computing.net/xor-encryption-algorithm/
def cipher(message, key):

    ciphered_message = []

    try:
        for i in range(len(message)):
            j = i % len(key)

            xor = message[i] ^ key[j]
            ciphered_message.append(xor)

        return ciphered_message
    except ZeroDivisionError:
        print("There is no valid key!")
