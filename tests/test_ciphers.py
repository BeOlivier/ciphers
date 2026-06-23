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
    assert caesar_encrypt("this is a harder test%&/()=?+", 67) == "iwxh xh p wpgstg ithi%&/()=?+"
    assert caesar_encrypt("ABC", 1) == "BCD"
    assert caesar_encrypt("XYZ", 3) == "ABC"
    assert caesar_encrypt("Hello, World!", 1) == "Ifmmp, Xpsme!"
    assert caesar_encrypt("abc", 27) == "bcd"
    assert caesar_encrypt("xyz", 29) == "abc"
    assert caesar_encrypt("abc", 0) == "abc"
    assert caesar_encrypt("abc", -1) == "zab"
    assert caesar_encrypt("", 5) == ""
    assert caesar_encrypt("123 !?", 10) == "123 !?"
    assert caesar_encrypt("ABS", 2) == "CDU"
    assert caesar_encrypt("z", 1) == "a"
    assert caesar_encrypt("Z", 1) == "A"
    assert caesar_encrypt("azAZ", 1) == "baBA"
    assert caesar_encrypt("middle", 26) == "middle"
    assert caesar_encrypt("middle", 52) == "middle"
    assert caesar_encrypt("middle", -26) == "middle"
    assert caesar_encrypt("abc", -27) == "zab"
    assert caesar_encrypt("xyz", -3) == "uvw"
    assert caesar_encrypt("Caesar Cipher 101!", 5) == "Hfjxfw Hnumjw 101!"

def test_caesar_decrypt():
    assert caesar_decrypt('bcd', 1) == 'abc'
    assert caesar_decrypt('abc', 3) == 'xyz'
    assert caesar_decrypt("ifmmp xpsme!", 1) == "hello world!"
    assert caesar_decrypt("iwxh xh p wpgstg ithi%&/()=?+", 67) == "this is a harder test%&/()=?+"
    assert caesar_decrypt("BCD", 1) == "ABC"
    assert caesar_decrypt("ABC", 3) == "XYZ"
    assert caesar_decrypt("Ifmmp, Xpsme!", 1) == "Hello, World!"
    assert caesar_decrypt("bcd", 27) == "abc"
    assert caesar_decrypt("abc", 29) == "xyz"
    assert caesar_decrypt("abc", 0) == "abc"
    assert caesar_decrypt("zab", -1) == "abc"
    assert caesar_decrypt("", 5) == ""
    assert caesar_decrypt("123 !?", 10) == "123 !?"
    assert caesar_decrypt("CDU", 2) == "ABS"
    assert caesar_decrypt("a", 1) == "z"
    assert caesar_decrypt("A", 1) == "Z"
    assert caesar_decrypt("baBA", 1) == "azAZ"
    assert caesar_decrypt("middle", 26) == "middle"
    assert caesar_decrypt("middle", 52) == "middle"
    assert caesar_decrypt("middle", -26) == "middle"
    assert caesar_decrypt("zab", -27) == "abc"
    assert caesar_decrypt("uvw", -3) == "xyz"
    assert caesar_decrypt("Hfjxfw Hnumjw 101!", 5) == "Caesar Cipher 101!"
