import string
alphabet_lc = string.ascii_lowercase*2
alphabet_uc = string.ascii_uppercase*2

def caesar_encrypt(plaintext, shift):
    # implement the caesar cipher encryption logic here
    ciphertext = ""
    for char in plaintext:
        # Switch each LETTER and transpose to new letter 
        # depending on what step was chosen
        if char in alphabet_lc:
            position = alphabet_lc.index(char) + shift
            ciphertext += alphabet_lc[position]
        elif char in alphabet_uc:
            ciphertext += alphabet_uc[position]
        else:
        # this is for punctuation
            ciphertext += char

    print(ciphertext)
    return ciphertext
def caesar_decrypt():
    # implement the caesar cipher decryption logic here
    return 0

caesar_encrypt("hello", -2)
