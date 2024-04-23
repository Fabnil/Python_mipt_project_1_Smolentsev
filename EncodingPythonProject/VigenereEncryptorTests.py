from VigenereEncryptor import VigenereEncryptor


def TestCase(path: str, key: str, inp: str, lang: str, res: str):
    enc = VigenereEncryptor(path, key, lang)
    with open(path, "r+") as file:
        file.truncate(0)
        file.seek(0)
        file.writelines(inp.split('\n'))
    enc.Encrypt()
    result_enc = ""
    with open(path, "r") as file:
        result_enc = '\n'.join(file.readlines())
    # print(result_enc, "||||", res)
    assert (result_enc == res)
    enc.Decrypt()
    result_dec = ""
    with open(path, "r") as file:
        result_dec = '\n'.join(file.readlines())
    assert (result_dec == inp)


def TestEnglish():
    TestCase("file_for_test_viginer.txt", "aboba",
             "abiba", "english",
             "acwca")
    TestCase("file_for_test_viginer.txt", "ab", "aboba bebra pivo", "english",
             "acoca bfbsa pjvp")
    TestCase("file_for_test_viginer.txt", "c", "x", "english", "z")
    alph = "abcdefghijklmnopqrstuvwxyz"
    for c in alph:
        TestCase("file_for_test_viginer.txt", c, "a" * 5, "english", c * 5)
    for i in range(0, len(alph)):
        for j in range(0, len(alph)):
            for sz in range(0, 10):
                TestCase("file_for_test_viginer.txt", alph[i], alph[j] * sz,
                         "english",
                         alph[(i + j) % len(alph)] * sz)
    for i in range(0, len(alph)):
        TestCase("file_for_test_viginer.txt", alph[i], alph, "english", "".join([alph[(x + i) % len(alph)] for x in range(0, len(alph))]))


def TestRussian():
    alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    for i in range(0, len(alph)):
        for j in range(0, len(alph)):
            for sz in range(0, 10):
                TestCase("file_for_test_viginer.txt", alph[i], alph[j] * sz,
                         "russian",
                         alph[(i + j) % len(alph)] * sz)
    TestCase("file_for_test_viginer.txt", "аб",
             "абоба", "russian",
             "авова")
    for i in range(0, len(alph)):
        TestCase("file_for_test_viginer.txt", alph[i], alph, "russian", "".join([alph[(x + i) % len(alph)] for x in range(0, len(alph))]))

TestEnglish()
TestRussian()
