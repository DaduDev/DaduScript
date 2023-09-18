from lexer import Integer, Float


class Interpreter:
    def __init__(self, tree, base):
        self.tree = tree
        self.data = base

    def interprete(self, tree=None):

        if tree is None:
            tree = self.tree

        if isinstance(tree, list) and len(tree) == 2:
            return self.compute_unary(tree[0], tree[1])

        elif not isinstance(tree, list):
            return tree

        else:

            left_node = tree[0]

            if isinstance(left_node, list):
                left_node = self.interprete(left_node)

            right_node = tree[2]

            if isinstance(right_node, list):
                right_node = self.interprete(right_node)

            operator = tree[1]
            return self.compute(left_node, operator, right_node)

    def compute_unary(self, operator, operand):
        operand_type = "VARIABLE" if str(operand.type).startswith(
            "VARIABLE") else str(operand.type)
        operand = getattr(self, f"read_{operand_type}")(operand.value)
        if operator.value == '+':
            return +operand
        elif operator.value == '-':
            return -operand

    def compute(self, left, operator, right):
        left_type = "VARIABLE" if str(left.type).startswith(
            "VARIABLE") else str(left.type)
        right_type = "VARIABLE" if str(right.type).startswith(
            "VARIABLE") else str(right.type)

        if operator.value == '=':
            left.type = f"VARIABLE({right_type})"
            self.data.write(left, right)
            return self.data.read_all()

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

    def read_VARIABLE(self, id):
        variable = self.data.read(id)
        variable_type = variable.type

        return getattr(self, f"read_{variable_type}")(variable.value)
