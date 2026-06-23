import string
alphabet_lc = string.ascii_lowercase
alphabet_uc = string.ascii_uppercase

def caesar_encrypt(plaintext, shift):
    # function encrypts plaintext to ciphertext
    # (while preserving original letter casing) using 
    # old fashioned Caesar cipher and a shift key, function 
    # is able to accept large negative and positive shifts

    ciphertext = ""
    
    for char in plaintext:
        # switch each LETTER and encrypt to new letter 
        # based on shift
        if char in alphabet_lc:
            index_new_letter = (alphabet_lc.index(char) + shift) % len(alphabet_lc)
            ciphertext += alphabet_lc[index_new_letter]
        elif char in alphabet_uc:
            index_new_letter = (alphabet_uc.index(char) + shift) % len(alphabet_uc)
            ciphertext += alphabet_uc[index_new_letter]
        else:
        # this is to preserve non-letters
            ciphertext += char

    return ciphertext

def caesar_decrypt(ciphertext, shift):
    # function decrypts ciphertext to plaintext preserving
    # original letter casing using Caesar cipher and a known
    # shift key, also able to accept large negative and positive shifts
    
    plaintext = ""
    
    for char in ciphertext:
        # switch each LETTER and decrypt to new letter 
        # based on shift
        if char in alphabet_lc:
            index_new_letter = (alphabet_lc.index(char) - shift) % len(alphabet_lc)
            plaintext += alphabet_lc[index_new_letter]
        elif char in alphabet_uc:
            index_new_letter = (alphabet_uc.index(char) - shift) % len(alphabet_uc)
            plaintext += alphabet_uc[index_new_letter]
        else:
        # this is to preserve non-letters
            plaintext += char

    return plaintext

def caesar_bruteforce(ciphertext):
    # implement a bruteforce that goes through every 
    # possible shift and returns them all in a list
    
    bruteforce = []
    
    for i in range(26):
        bruteforce.append((i, caesar_decrypt(ciphertext, i)))
        
    return bruteforce

caesar_bruteforce("iwxh xh p wpgstg ithi%&/()=?+")