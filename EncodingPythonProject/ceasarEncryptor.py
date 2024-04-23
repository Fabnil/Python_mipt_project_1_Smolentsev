import copy

from VigenereEncryptor import VigenereEncryptor
from alphabets import RuAlphabetSmall
from alphabets import EngAlphabetSmall

class CeasarEncryptor(VigenereEncryptor):
    def __init__(self, file_path: str, move_cnt: int, lang: str):
        assert (lang == "russian" or lang == "english")
        alph = copy.deepcopy(
            RuAlphabetSmall if lang == "russian" else EngAlphabetSmall)
        super().__init__(file_path, alph[move_cnt % len(alph)], lang)
