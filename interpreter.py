from lexer import Integer, Float


class Interpreter:
    def __init__(self, tree):
        self.tree = tree

    def interprete(self, tree=None):

        if tree is None:
            tree = self.tree

        left_node = tree[0]

        if isinstance(left_node, list):
            left_node = self.interprete(left_node)

        right_node = tree[2]

        if isinstance(right_node, list):
            right_node = self.interprete(right_node)

        operator = tree[1]
        return self.compute(left_node, operator, right_node)

    def compute(self, left, operator, right):
        left_type = left.type
        right_type = right.type

        left = getattr(self, f"read_{left_type}")(left.value)
        right = getattr(self, f"read_{right_type}")(right.value)

        if (operator.value == '+'):
            output = left+right
        elif (operator.value == '-'):
            output = left-right
        elif (operator.value == '*'):
            output = left*right
        elif (operator.value == '/'):
            output = left/right
        elif (operator.value == '%'):
            output = left % right

        return Integer(output) if (left_type == "INT" and right_type == "INT") else Float(output)

    def read_INT(self, value):
        return int(value)

    def read_FLOAT(self, value):
        return float(value)
