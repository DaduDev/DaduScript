from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

while True:
    text = input("DaduScript: ")
    tokeniser = Lexer(text)
    tokens = tokeniser.tokenize()

    parser = Parser(tokens)
    tree = parser.parse()

    interpreter = Interpreter(tree)
    result = interpreter.interprete()

    print(result)
