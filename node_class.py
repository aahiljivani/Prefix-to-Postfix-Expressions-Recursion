class Node:
    """
    A simple implementation of a node in an expression tree. Each node represents an element in the expression,
    which could be an operand (ASCII character) or an operator ( '+', '-', '*', '/', '$').
    This class is designed to facilitate the construction and manipulation of the expression tree by providing
    easy access to the node's value and its left and right children, which represent the operands for binary operations.

    Attributes:
        value (str): The value stored in this node, which can be an operator or an operand.
        left (Node): The left child of this node in the expression tree.
        right (Node): The right child of this node in the expression tree.

    Methods:
        __init__(self, char):
            Initializes a new instance of the Node class. The 'char' parameter is expected to be a string
            representing that node's value. The left and right children are initialized as None, indicating
            that this node has no children yet.

        isOperator(self):
            Determines if the node's value is an operator. Returns True if the value is one of the
            operator symbols ('$','*','/','+','-'), Returns False otherwise, indicating that this node
            is likely an operand.

        isValid(self):
            Validates the structural integrity of the expression tree from the root node all the way down to
            the end of the expression tree. The function checks if the current node is an operator, it must
            have both left and right children to be a valid prefix expression. A ValueError is raised with
            a message indicating why the tree is not valid if this is the case.

    This class is designed to build expression trees to be used in evaluating prefix expressions,
    and converting them into postfix expressions in a recursive manner.
    """

    def __init__(self, char):
        self.value = char
        self.left = None
        self.right = None

    def isOperator(self):
        operators = set(['$', '*', '/', '+', '-'])
        if self.value == '^':
            self.value = '$'
            return self.value in operators
        else:
            return self.value in operators

    def isValid(self):
        # If the node is an operator, ensure it has both left and right children nodes.
        if self.isOperator():
            if self.left is None or self.right is None:
                raise ValueError(f"Invalid Expression: Operator Node '{self.value}' does not have 2 children.")
            # Recursively check the validity of the left and right subtrees.
            self.left.isValid()
            self.right.isValid()
        # If the node is not an operator, it's considered a valid leaf node.
        return True
