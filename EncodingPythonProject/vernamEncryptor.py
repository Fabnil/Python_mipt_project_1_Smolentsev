from encryptorByInvolution import EncryptorByInvolution
from alphabets import RuLetterMover, EngLetterMover


class VernamEncryptor(EncryptorByInvolution):
    path: str
    key: str

    def __init__(self, path_inp: str, key_inp: str):
        self.path = path_inp
        self.key = key_inp

    def MakeInvolution(self):
        key_ord = ord(self.key)
        ans = ""
        with open(self.path, "r+") as file:
            for line in file.readlines():
                for cur in line:
                    print(cur)
                    if ord(cur) in [ord('\n'), ord('\r'), ord('\n') ^ key_ord, ord('\r') ^ key_ord]:
                        ans += cur
                    else:
                        ans += chr(ord(cur) ^ key_ord)
            file.truncate(0)
            file.seek(0)
            file.write(ans)
