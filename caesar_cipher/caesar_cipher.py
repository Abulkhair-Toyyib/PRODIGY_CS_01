letters = "abcdefghijklmnopqrstuvwxyz"
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        letter = letter.lower()
        if letter == " ":
            ciphertext += " "
        else:
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter  # Keep non-alphabet characters unchanged
            else:
                new_index = (index + key) % num_letters
                ciphertext += letters[new_index]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        letter = letter.lower()
        if letter == " ":
            plaintext += " "
        else:
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = (index - key) % num_letters
                plaintext += letters[new_index]
    return plaintext

def encrypt_decrypt(text, mode, key):
    result = ""
    if mode == "d":
        key = -key
    
    for letter in text:
        letter = letter.lower()
        if letter == " ":
            result += " "
        else:
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = (index + key) % num_letters
                result += letters[new_index]
    return result

print()
print("*** CAESAR CIPHER PROGRAM ***")
print()

print("Do you want to encrypt or decrypt?..")
user_input = input("e/d: ").lower()

if user_input == "e":
    print("ENCRYPTION MODE SELECTED")
    print()
    key = int(input("Enter the key (1 through 26): "))
    text = input("Enter the text to encrypt: ")
    ciphertext = encrypt(text, key)
    print(f'CIPHERTEXT: {ciphertext}')
    
elif user_input == "d":
    print("DECRYPTION MODE SELECTED")
    print()
    key = int(input("Enter the key (1 through 26): "))
    text = input("Enter the text to decrypt: ")
    plaintext = decrypt(text, key)
    print(f'PLAINTEXT: {plaintext}')
  
