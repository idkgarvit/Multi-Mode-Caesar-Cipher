from word2number import w2n

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encryption(text, shift):
    cipher_text = ""
    for char in text:
        if char in LOWERCASE:
            index = LOWERCASE.index(char)
            new_index = (index - shift) % 26
            cipher_text += LOWERCASE[new_index]
        elif char in UPPERCASE:
            index = UPPERCASE.index(char)
            new_index = (index - shift) % 26
            cipher_text += UPPERCASE[new_index]
        else:
            cipher_text += char
    return cipher_text

def decryption(cipher_text, shift):
    plaintext = ""
    for char in cipher_text:
        if char in LOWERCASE:
            index = LOWERCASE.index(char)
            new_index = (index + shift) % 26
            plaintext += LOWERCASE[new_index]
        elif char in UPPERCASE:
            index = UPPERCASE.index(char)
            new_index = (index + shift) % 26
            plaintext += UPPERCASE[new_index]
        else:
            plaintext += char
    return plaintext

def brute_force(cipher_text):
    print("\n...... Brute force results ......")
    for key in range(26):
        print(f"Key {key}: {decryption(cipher_text, key)}")

mode = input("Do you want to (E)ncrypt, (D)ecrypt, (B)oth, or (BF) brute force? ").lower()

if mode.startswith("bf"):
    cipher_txt = input("Enter the cipher text to brute force: ")
    brute_force(cipher_txt)

else:
    plaintext = input("Enter the text: ")
    shift_input = input("Enter the key value : ")

    try:
        shift = int(shift_input)
    except ValueError:
        try:
            shift = w2n.word_to_num(shift_input)
        except ValueError:
            print("Invalid input. Please enter a number or number word.")
            exit()

    if mode.startswith("e"):
        print("Encrypted:", encryption(plaintext, shift))
    elif mode.startswith("d"):
        print("Decrypted:", decryption(plaintext, shift))
    elif mode.startswith("b"):
        encrypted = encryption(plaintext, shift)
        print("Encrypted:", encrypted)
        decrypted = decryption(encrypted, shift)
        print("Decrypted:", decrypted)
    else:
        print("Invalid mode. Choose E, D, B, or BF.")