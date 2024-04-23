from alphabets import RuAlphabetSmall
from alphabets import EngAlphabetSmall
from ceasarEncryptor import CeasarEncryptor
import collections


class CeasarHacker:
    encr: CeasarEncryptor

    def mostPopularLetterInFile(self, path: str,
                                lang: str) -> str:  # маленькая буква
        assert (lang == "russian" or lang == "english")
        small_alph_set = set(
            RuAlphabetSmall if lang == "russian" else EngAlphabetSmall);
        file_as_str = ""
        with open(path, "r+") as file:
            for line in file.readlines():
                file_as_str += line
        return collections.Counter(
            file_as_str.filter(lambda x: (x.lower() in small_alph_set),
                               file_as_str)).most_common(1)[0][0]

    def __init__(self, path: str, lang: str):
        assert (lang == "russian" or lang == "english")
        encr = CeasarEncryptor(path, ord(self.mostPopularLetterInFile(path,
                                                                      lang)) - ord(
            RuAlphabetSmall[0] if lang == "russian" else EngAlphabetSmall[0]),
                               lang)

    def Hack(self):
        self.encr.Decrypt()
