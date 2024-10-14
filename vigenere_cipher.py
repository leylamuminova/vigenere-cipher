# vigenere-cipher
#Practiced the Vigenère cipher concepts of encrypting and decrypting messages using a key.
import random 

def generate_key(length):
    """Generating a random string"""
    letters = "abcdefghijklmnopqrstuvwxyz"
    key = ""
    for i in range (length):
        key += random.choice(letters)
    return key

def encrypt(key, message):
    """Encrypting a message"""
    new_cipher = ""
    for i in range(len(key)):
        m_pos = ord(message[i]) - ord("a")
        k_pos = ord(key[i]) - ord("a")
        cipher = (m_pos + k_pos) % 26
        new_cipher += chr(cipher + ord("a"))
    
    return new_cipher

def decrypt(key, new_cipher):
    """Decrypting a message"""
    new_message = ""
    for j in range(len(new_cipher)):
        c_pos = ord(new_cipher[j]) - ord("a")
        k_pos = ord(key[j]) - ord("a")
        message = (c_pos - k_pos) % 26
        new_message += chr(message + ord("a"))

    return new_message
    
def main():
    message = input("Message?: ").lower()
    length = len(message)  # Set key length to the length of the message
    key = generate_key(length)
    new_cipher = encrypt(key, message)
    decrypted_message = decrypt(key, new_cipher)

    # Print results in the expected format
    print(f"Key: {key}")
    print(f"Encrypted: {new_cipher}")
    print(f"Decrypted: {decrypted_message}")

main()
