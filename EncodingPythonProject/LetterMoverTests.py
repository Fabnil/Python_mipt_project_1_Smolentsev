from alphabets import OneLetterMover
from alphabets import RuLetterMover
from alphabets import EngLetterMover

class OneLetterMoverTester:
    def Test(self, alph: str, mover: OneLetterMover):
        # IsLetterFromAlphabet
        for c in alph:
            assert (mover.IsLetterFromAlphabet(c))
        for i in range(0, 256):
            assert (mover.IsLetterFromAlphabet(chr(i)) == (
                (chr(i) in alph.lower()) or (chr(i) in alph.upper())))

        # index_of_letter
        for c in alph:
            assert (mover.index_of_letter(c) == alph.find(c))
            assert (mover.index_of_letter(c.upper()) == mover.index_of_letter(c.lower()))

        # AlphabetSize
        assert (mover.AlphabetSize() == len(alph))

        # SymmetricLetter
        for i in range(0, len(alph)):
            assert (mover.SymmetricLetter(alph[i]) == alph[-1 - i])

        # MovedLetter
        for move_cnt in range(0, len(alph) * 2 + 1):
            for i in range(0, len(alph)):
                assert (mover.MovedLetter(alph[i], move_cnt) == alph[
                    (((i + move_cnt) % len(alph)) + len(alph)) % len(alph)])

    def TestAllCaces(self):
        self.Test("абвгдеёжзийклмнопрстуфхцчшщъыьэюя", RuLetterMover)
        self.Test("абвгдеёжзийклмнопрстуфхцчшщъыьэюя".upper(), RuLetterMover)
        self.Test("abcdefghijklmnopqrstuvwxyz", EngLetterMover)
        self.Test("abcdefghijklmnopqrstuvwxyz".upper(), EngLetterMover)

OneLetterMoverTester().TestAllCaces()