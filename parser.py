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

    def parse(self):
        return self.expression()

    def advance(self):
        self.idx += 1
        if self.idx < len(self.tokens):
            self.token = self.tokens[self.idx]
