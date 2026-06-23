import string
alphabet_lc = string.ascii_lowercase*2
alphabet_uc = string.ascii_uppercase*2

def caesar_encrypt(plaintext, shift):
    # this function encrypts plaintext to ciphertext
    # (while preserving original letter casing) using 
    # old fashioned Caesar cipher and a shift key function 
    # is able to accept large negative and positive shifts

    ciphertext = ""
    shift %= 26
    
    for char in plaintext:
        # switch each LETTER and encrypt to new letter 
        # based on shift
        if char in alphabet_lc:
            position = alphabet_lc.index(char) + shift
            ciphertext += alphabet_lc[position]
        elif char in alphabet_uc:
            position = alphabet_uc.index(char) + shift
            ciphertext += alphabet_uc[position]
        else:
        # this is for special chars and emptyspaces
            ciphertext += char

    return ciphertext

def caesar_decrypt(ciphertext, shift):
    # implement the caesar cipher decryption logic here
    plaintext = ""
    shift %= 26
    
    for char in ciphertext:
        # switch each LETTER and encrypt to new letter 
        # based on shift
        if char in alphabet_lc:
            position = alphabet_lc.index(char) - shift
            plaintext += alphabet_lc[position]
        elif char in alphabet_uc:
            position = alphabet_uc.index(char) - shift
            plaintext += alphabet_uc[position]
        else:
        # this is for special chars and emptyspaces
            plaintext += char

    return plaintext

def caesar_bruteforce(ciphertext):
    # implement a bruteforce that goes through every 
    # possible shift and returns them all in a list
    return 0
