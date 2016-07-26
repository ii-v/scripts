#!/usr/bin/env python3
from random import randrange

def encode(message):
    """Converts letters to numbers"""
    encoded_message = []
    for letter in message:
        number = ord(letter)
        encoded_message.append(number)
    return encoded_message

def generate_key(encoded_message):
    """Generates a key to encrypt and decrypt the message"""
    key = []
    for n in encoded_message:
        key.append(randrange(1,100))
    return key

def xor_function(message, key, mode):
    """Does the encryption and decryption by XOR:ing the message and the key"""
    if mode == "encrypt":
        encrypted_message = []
        for index, number in enumerate(message):
            encrypted_message.append(number ^ key[index])
        return encrypted_message
    elif mode == "decrypt":
        decrypted_message = []
        for index, number in enumerate(message):
            decrypted_message.append(key[index] ^ number)
        return decrypted_message
    return "Invalid input"
     
def decode(encoded_message):
    """Converts numbers to letters"""
    message = []
    for number in encoded_message:
        letter = chr(number)
        message.append(letter)
    return message

def encrypt(message):
    """Links all functions together and encrypts a message"""
    encoded = encode(message)
    key = generate_key(encoded)
    encrypted = xor_function(encoded, key, "encrypt")
    print("Encrypted message: " + str(encrypted))
    print("Key: " + str(key))

def decrypt(encrypted_message, key):
    """Decrypts a message"""
    encoded_message = xor_function(encrypted_message, key, "decrypt")
    decrypted_message = decode(encoded_message)
    return ''.join(decrypted_message)
