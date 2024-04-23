import copy

class OneLetterMover:
    small_alphabet: str
    big_alphabet: str
    small_alphabet_dict: dict
    big_alphabet_dict: dict

    def __init__(self, small_alphabet_for_move: str):
        self.small_alphabet = copy.deepcopy(
            small_alphabet_for_move.lower())
        self.big_alphabet = copy.deepcopy(
            self.small_alphabet.upper())
        self.small_alphabet_dict = {}
        self.big_alphabet_dict = {}
        for i in range(0, len(self.small_alphabet)):
            self.small_alphabet_dict[self.small_alphabet[i]] = i
            self.big_alphabet_dict[self.big_alphabet[i]] = i

    def IsLetterFromAlphabet(self, letter: str) -> bool:
        return ((letter in self.small_alphabet_dict) or
                (letter in self.big_alphabet_dict))

    def index_of_letter(self, letter: str) -> int:
        assert (self.IsLetterFromAlphabet(letter))
        if letter in self.small_alphabet_dict:
            return self.small_alphabet_dict[letter]
        elif letter in self.big_alphabet_dict:
            return self.big_alphabet_dict[letter]

    def AlphabetSize(self) -> int:
        return len(self.small_alphabet)

    def SymmetricLetter(self, letter: str) -> str:
        index = self.index_of_letter(letter)
        if letter in self.small_alphabet_dict:
            return self.small_alphabet[-1 - index]
        else:
            return self.big_alphabet[-1 - index]

    # возвращает сдвинутую по циклу букву в зависимости от её регистра (то есть регистр сохраняется)
    def MovedLetter(self, letter: str, move_cnt: int) -> str:
        assert (self.IsLetterFromAlphabet(letter))
        sz = len(self.small_alphabet)
        if letter in self.small_alphabet_dict:
            cur_index = self.small_alphabet_dict[letter]
            return self.small_alphabet[
                (((cur_index + move_cnt) % sz) + sz) % sz]
        if letter in self.big_alphabet_dict:
            cur_index = self.big_alphabet_dict[letter]
            return self.big_alphabet[(((cur_index + move_cnt) % sz) + sz) % sz]


RuAlphabetSmall = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
EngAlphabetSmall = "abcdefghijklmnopqrstuvwxyz"

RuLetterMover = OneLetterMover("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
EngLetterMover = OneLetterMover("abcdefghijklmnopqrstuvwxyz")
