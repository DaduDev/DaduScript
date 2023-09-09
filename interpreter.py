class Interpreter:
    def __init__(self, tree):
        self.tree = tree

    def interprete(self):
        left_node = self.tree[0]
        right_node = self.tree[2]
        operator = self.tree[1]
        return self.compute(left_node, operator, right_node)

    def compute(self, left, operator, right):
        if (left.type == 'INT'):
            left = int(left.value)
        elif (left.type == 'FLOAT'):
            left = float(left.value)
        if (right.type == 'INT'):
            right = int(right.value)
        elif (right.type == 'FLOAT'):
            right = float(right.value)
        if (operator.value == '+'):
            return left+right
