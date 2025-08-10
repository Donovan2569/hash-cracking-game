import string
import base64

# Easy mode
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            letter_pos = ord(char) - ascii_offset
            if mode == 'encrypt':
                new_pos = (letter_pos + shift) % 26
            elif mode == 'decrypt':
                new_pos = (letter_pos - shift) % 26
            result += chr(new_pos + ascii_offset)
        else:
            result += char
    return result

# Medium mode
def xor(text, key, mode = 'encrypt'):
    key_bytes = key.encode('utf-8')
    key_len = len(key_bytes)

    if mode == 'encrypt':
        text_bytes = text.encode('utf-8')
        xor_bytes = bytes([text_bytes[i] ^ key_bytes[i % key_len] for i in range(len(text_bytes))])
        return base64.b64encode(xor_bytes).decode('utf-8')

    elif mode == 'decrypt':
        xor_bytes = base64.b64decode(text)
        original_bytes = bytes([xor_bytes[i] ^ key_bytes[i % key_len] for i in range(len(xor_bytes))])
        return original_bytes.decode('utf-8')
    
# Hard mode
def vigenere(text, key, mode='encrypt'):
    alphabet = string.ascii_lowercase
    Alphabet = string.ascii_uppercase
    count = 0
    result = ""
    key = key.lower()
    for letter in text:
        if letter in alphabet:
            key_index = alphabet.index(key[count])
            letter_index = alphabet.index(letter)
            if mode == 'encrypt':
                new_index = (letter_index + key_index) % 26
            else:
                new_index = (letter_index - key_index + 26) % 26
            result += chr(97 + new_index)
            count += 1
        elif letter in Alphabet:
            key_index = alphabet.index(key[count])
            letter_index = Alphabet.index(letter)
            if mode == 'encrypt':
                new_index = (letter_index + key_index) % 26
            else:
                new_index = (letter_index - key_index + 26) % 26
            result += chr(65 + new_index)
            count += 1
        else:
            result += letter
        if count >= len(key):
            count = 0
    return result