from vernamEncryptor import VernamEncryptor


def Test(letter : str):
    enc = VernamEncryptor("file_for_test_vernam.txt", letter)
    enc.Encrypt()
    enc.Decrypt()
Test("a")
Test("b")
Test("Z")
Test("л")
Test("ф")
Test("Ж")