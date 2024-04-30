from VigenereEncryptor import VigenereEncryptor
from ceasarEncryptor import CeasarEncryptor

for key in range(0, 50):
    biba = CeasarEncryptor("file_for_test_ceasar.txt", key, "russian")
    biba.Encrypt()
    biba.Decrypt()
