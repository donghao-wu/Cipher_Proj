def caesar_cipher_decode(encoded_text, shift):
    """
    Decodes a Caesar Cipher encoded string.

    :param encoded_text: The encoded string to decode.
    :param shift: The number of positions each letter was shifted in the cipher.
    :return: The decoded string.
    """
    decoded_text = ""

    for char in encoded_text:
        if char.isalpha():  # Check if character is a letter
            start = ord('A') if char.isupper() else ord('a')
            decoded_char = chr((ord(char) - start - shift) % 26 + start)
            decoded_text += decoded_char
        else:
            decoded_text += char  # Non-alphabet characters remain unchanged
    return decoded_text
