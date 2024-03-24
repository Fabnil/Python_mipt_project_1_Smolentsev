# Описание проекта

Шифрование. Я буду реализовывать этот проект. Я сделаю консольное приложение,
которое умеет зашифровывать (и дешифровывать) файлы 3 шифрами: Цезаря, Виженера и Вернама.
Также можно будет автоматически взламывать Шифр Цезаря методом частотного анализа.

## Будет 7 функций:

а) Зашифровать / расшифровать шифром Цезаря: надо будет передавать сдвиг и путь к txt файлу
в котором должны будут находиться строго текст на русском или на Английском языке. Язык также нужно передать.
Если в файле будут символы, которые не попадают в интересующий алфавит, то шифра не произойдёт, и пользователь
узнает о проблеме. Шифрование / расшифрование будет происходить in-place, то есть в том же файле,
который передан как аргумент.

б) Зашифровать / расшифровать шифром Виженера: Требования те же (+ язык ключевого слова и язык файла должны совпадать),
что к шифру цезаря, и формат подачи аргументов тот же.
Только вместо Сдвига нужно передать ключевое слово.

в) Зашифровать / расшифровать шифром Вернама. Формат аргументов: ключевой символ (с ним будут xor-иться) и путь к файлу.
Требования к файлу: это должен быть txt файл из символов из таблицы ASCII. 
Ключевой символ как семибитное число будет xor-иться с каждым из символов как при шифровке, так и при дешифровке.

г) Взлом шифра цезаря. Нужно передать путь к файлу и язык (русский / английский). Этот файл будет in-place взломан.
Либо (в случае наличия проблемных символов) - это будет сказано юзеру.

## Архитектура

Будут сделаны такие классы / интерфейсы:

- **(interface) Encryptor** с 2 методами: Encrypt() и Decrypt()
- **(interface) EncryptorByInvolution** - реализует Encryptor с 1 доп. методом: MakeInvolution(), и он будет в Encrypt() и Decrypt()
просто вызывать MakeInvolution()
- **(class) CaesarMover** - служебный класс. У него будет конструктор от 3 параметров: пути к файлу, сдвига, и языка (строка: russian или english в нашем случае) Будет метод Move() - он будет in-place в файле сдвигать все символы языка на сдвиг. Он кинет исключение, если что не так.
- **(class) CaesarEncryptor** - реализует Encryptor. У него будет 2 поля CaesarMover: coder и decoder. У него будет конструктор от 3 аргументов: пути к файлу, сдвига, и языка. Он будет конструировать coder(файл, +сдвиг, язык) и decoder(файл, -сдвиг, язык) Encrypt() { coder.Move() }, Decrypt() { decoder.Move() }
- **(class) VigenereEncryptor** - реализует Encryptor. Конструируется от пути к файлу, ключевого слова и языка.
Будет приватный метод Move(bool invertedMove) - и он будет сдвигать по слову либо вперёд, либо назад (назад <=> invertedMove)
Тогда Encrypt() { Move(False) }, Decrypt() { Move(true) }

- **(class) VermanEncryptor()** - реализует EncryptorByInvolution. Создаётся от символа и пути к файлу, и его MakeInvolution() значит сделать xor= к каждому символу. Если какой-то символ не из ASCII - поведение не определено

- **(class) CaesarHacker** - взломщик шифра цезаря. Он конструируется от 2 параметров: пути к файлу и языка. 
У него будет поле CaesarMover mover и 1 метод: Hack() { 
Он, вычислив сдвиг методом частотного анализа, сделает mover-а CaesarMover с нужным сдвигом и скажет Move() 
}

Ну и в итоге в main() будет происходить объединение всего этого в то, что нужно. Будет считываться то, что ввёл юзер, и сделано
то, что он просил.


