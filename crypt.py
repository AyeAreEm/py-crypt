from string import ascii_lowercase

LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=0)}
NUMBER = []

class Encrypt:
    def __init__(self, text):
        self.text = text

    def alpha_pos(self):
        numbers = [LETTERS[character] for character in self.text.lower() if character in LETTERS]
        global NUMBER
        NUMBER = numbers

        return ' '.join(numbers)

class Decrypt:
    def __init__(self, encrypted):
        self.encrypted = encrypted

    def pos_to_char(self):
        self.encrypted = list(map(int, self.encrypted))
        decrypted = []

        for i in range(0, len(self.encrypted)):
            decrypt = ascii_lowercase[self.encrypted[i]]
            decrypted.append(decrypt)

        return ' '.join(decrypted)

text = input("Enter text: ")
encrypted = Encrypt(text).alpha_pos()
print(encrypted)

print(Decrypt(NUMBER).pos_to_char())