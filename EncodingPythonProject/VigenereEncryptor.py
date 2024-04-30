import copy

from encriptor import Encryptor
from alphabets import RuLetterMover
from alphabets import EngLetterMover

class VigenereEncryptor(Encryptor):
    path: str  # полный путь до файла
    key: str
    lang: str  # может принимать значение russian и english

    def __init__(self, file_path: str, key_word: str, language: str):
        self.path = file_path
        self.key = key_word
        self.lang = language
        assert (self.lang == "english" or self.lang == "russian")

    def Move(self, invertedMove: bool):
        with open(self.path, "r+") as file:
            CurMover = RuLetterMover if self.lang == "russian" else (
                EngLetterMover if self.lang == "english" else None)
            assert (not (CurMover is None))
            cnt = 0
            ans = []  # массив строк, которые надо будет записать
            for cur_line in file.readlines():
                line = copy.deepcopy(list(cur_line))
                for i in range(0, len(line)):
                    if line[i] == '\n':
                        continue
                    if CurMover.IsLetterFromAlphabet(line[i]):
                        cur_index = CurMover.index_of_letter(self.key[cnt])
                        move_cnt = ((CurMover.AlphabetSize() - cur_index) % CurMover.AlphabetSize() if invertedMove else cur_index)
                        line[i] = CurMover.MovedLetter(line[i], move_cnt)
                    cnt += 1
                    cnt %= len(self.key)
                ans.append("".join(line))
            #print("ans:", ans)
            file.truncate(0)
            file.seek(0)
            file.writelines(ans)

    def Encrypt(self):
        self.Move(False)

    def Decrypt(self):
        self.Move(True)