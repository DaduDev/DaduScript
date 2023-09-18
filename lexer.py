class Lexer:
    digits = "0123456789"
    operations = "+-/*%()="
    letters = "abcdefhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    declarations = ["make", "let", "variable"]
    stopwards = [" "]
    boolean = ["and", "or", "not"]

    def __init__(self, text):
        self.text = text
        self.idx = 0
        self.tokens = []
        self.char = self.text[self.idx]
        self.token = None

    def tokenize(self):
        while (self.idx < len(self.text)):
            if self.char in Lexer.digits:
                self.token = self.extract_number()
            elif self.char in Lexer.operations:
                self.token = Operation(self.char)
                self.advance()
            elif self.char in Lexer.stopwards:
                self.advance()
                continue
            elif self.char in Lexer.letters:
                word = self.extract_word()
                if word in Lexer.declarations:
                    self.token = Declaration(word)
                else:
                    self.token = Variable(word)
            elif word in Lexer.boolean:
                self.token = Boolean(word)

            self.tokens.append(self.token)

        return self.tokens

    def extract_number(self):
        number = ""
        isFloat = False
        while (self.char in Lexer.digits or self.char == ".") and (self.idx < len(self.text)):
            if self.char == ".":
                isFloat = True
            number += self.char
            self.advance()

        return Integer(number) if not isFloat else Float(number)

    def extract_word(self):
        word = ""
        while (self.char in Lexer.letters and self.idx < len(self.text)):
            word += self.char
            self.advance()
        return word

    def advance(self):
        self.idx += 1
        if self.idx < len(self.text):
            self.char = self.text[self.idx]


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return str(self.value)


class Integer(Token):
    def __init__(self, value):
        super().__init__("INT", value)


class Float(Token):
    def __init__(self, value):
        super().__init__("FLOAT", value)


class Operation(Token):
    def __init__(self, value):
        super().__init__("OPERATION", value)


class Declaration(Token):
    def __init__(self, value):
        super().__init__("DECLARATION", value)


class Variable(Token):
    def __init__(self, value):
        super().__init__("VARIABLE(?)", value)


class Boolean(Token):
    def __init__(self, value):
        super().__init__("BOOLEAN", value)
