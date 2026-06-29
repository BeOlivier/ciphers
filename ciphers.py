import caesar
from caesar import caesar_bruteforce, caesar_decrypt, caesar_encrypt

def main():
    # show menu
    choice = input("Please choose one of the following ciphers\n"
                   +"1 = Caesar\n2 = Vigenere\n3 = Cooming soon...\n")
    
    # ask user for encryption or decryption
    action = input("1 = Encryption\n2 = Decryption\n3 = Bruteforce\n")
    
    # ask for the shift value
    if action != "3":
        key = int(input("input key for encryption/decryption if you have one: "))
    
    # ask for the text
    text = input("Ciphertext/Plaintext:\n")
    
    # call function to encrypt/decrypt/bruteforce
    match choice:
         case "1":
            if action == "1":
                print(caesar_encrypt(text, key))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())