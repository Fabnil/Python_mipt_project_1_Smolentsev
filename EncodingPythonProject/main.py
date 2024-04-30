from colorama import init, Fore, Back, Style
from ceasarEncryptor import CeasarEncryptor
from VigenereEncryptor import VigenereEncryptor
from vernamEncryptor import VernamEncryptor
from ceasarHacker import CeasarHacker


def main() -> None:
    init(autoreset=True)
    work_mode = int(input(
        Style.BRIGHT + Back.YELLOW + Fore.BLACK + "Выберите шифр. 1 - Шифр Цезаря, 2 - Шифр Вижинера, 3 - Шифр Вернама, 4 - Взлом шифра цезаря "))
    assert (1 <= work_mode <= 4)
    path = input(
        Style.BRIGHT + Back.YELLOW + Fore.BLACK + "Теперь введите путь к файлу. ")
    lang = input(
        Style.BRIGHT + Back.YELLOW + Fore.BLACK + "Введите язык. (russian если русский, english иначе) ")
    if work_mode == 4:
        hacker = CeasarHacker(path, lang)
        hacker.Hack()
        return None
    key = input(
        Style.BRIGHT + Back.YELLOW + Fore.BLACK + "Введите ключ (сдвиг в случае шифра Цезаря) ")
    enc = None
    if work_mode == 1:
        key = int(key)
        enc = CeasarEncryptor(path, key, lang)
    elif work_mode == 2:
        enc = VigenereEncryptor(path, key, lang)
    elif work_mode == 3:
        enc = VernamEncryptor(path, key)
    to_encrypt = (input(
        Style.BRIGHT + Back.YELLOW + Fore.BLACK + "Введите 1 если хотите зашифровать файл и 0 иначе. ") == "1")
    if to_encrypt:
        enc.Encrypt()
    else:
        enc.Decrypt()
    print(Style.BRIGHT + Back.YELLOW + Fore.BLACK + "Всё успешно! ")


main()
