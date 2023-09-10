class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.idx = 0
        self.token = self.tokens[self.idx]

    def factor(self):
        if (self.token.type == "INT" or self.token.type == "FLOAT"):
            return self.token
        elif (self.token.value == '('):
            self.advance()
            expression = self.expression()
            return expression

    def term(self):
        left_node = self.factor()
        self.advance()
        output = left_node
        if self.token.value == '*' or self.token.value == '/':
            operation = self.token
            self.advance()
            right_node = self.factor()
            self.advance()
            output = [left_node, operation, right_node]

        return output

    def expression(self):
        left_node = self.term()
        while self.token.value == '+' or self.token.value == '-':
            operation = self.token
            self.advance()
            right_node = self.term()
            left_node = [left_node, operation, right_node]

        return left_node

    def variable(self):
        if self.token.type == "VARIABLE":
            return self.token

    def statement(self):
        if self.token.type == "DECLARATION":
            self.advance()
            left_node = self.variable()
            self.advance()
            if self.token.value == "=":
                operation = self.token
                self.advance()
                right_node = self.expression()
                return [left_node, operation, right_node]

        elif self.token.type == "INT" or self.token.type == "FLOAT" or self.token.type == "OPERATION":
            return self.expression()

    def parse(self):
        return self.statement()

    def advance(self):
        self.idx += 1
        if self.idx < len(self.tokens):
            self.token = self.tokens[self.idx]
