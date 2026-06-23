import caesar

# Caesar cipher tests

def test_caesar_encrypt_function_exists():
    assert hasattr(caesar, "caesar_encrypt")

def test_caesar_decrypt_function_exists():
    assert hasattr(caesar, "caesar_decrypt")

from caesar import caesar_encrypt, caesar_decrypt

def test_caesar_encrypt():
    assert caesar_encrypt("abc", 1) == "bcd"
    assert caesar_encrypt("xyz", 3) == "abc"
    assert caesar_encrypt("hello world!", 1) == "ifmmp xpsme!"

# def test_caesar_decrypt():
#     assert caesar_decrypt('bcd', 1) == 'abc'
#     assert caesar_decrypt('abc', 3) == 'xyz'
#     assert caesar_decrypt("ifmmp xpsme!", 1) == "hello world!"
