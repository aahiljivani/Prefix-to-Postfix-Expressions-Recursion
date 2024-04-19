from .node_class import Node
def process_inputfile(input_file, output_file):
    """
    Reads each prefix expression from the input_file, strips the line of any whitespace and converts it to postfix.
    The function writes the echoed prefix expression and postfix result to the output_file.
    """
    for liner in input_file:
        # Remove leading,trailing  and 'in between' whitespace
        line = liner.strip().replace(" ", "")
        # Check if the line is not empty
        if line:
            try:
                # Convert line from prefix to postfix expression
                tree = expression_tree(line)
                postfix_expression = conversion(tree)
                # write to the output file: prefix expression : postfix expression
                output_file.write('Prefix Expression is ' + line + ':\n' + 'Postfix Expression is ' + postfix_expression + '\n')
            # Allow ValueErrors and write them to the output file line corresponding to the input.txt
            except ValueError as e:
                output_file.write(str(e) + '\n')


def construct_nodes(prefix, index=0):
    if index >= len(prefix):
        return None, index

    # Create a new node from the current character.
    character = Node(prefix[index])

    if not character.isOperator():
        # For characters that are operands, return the node and the next index.
        return character, index + 1
    else:
        # For operator nodes, recursively construct the left and right children.
        character.left, newIndexLeft = construct_nodes(prefix, index + 1)
        character.right, newIndexRight = construct_nodes(prefix, newIndexLeft)

        # Ensure both children are present.
        if character.left is None or character.right is None:
            raise ValueError(
                f"Invalid Expression: Operator Node '{character.value}' does not have 2 children. Add operand(s).")

        return character, newIndexRight


def expression_tree(prefix):
    tree, index = construct_nodes(prefix)
    # After constructing the tree, this is a check to see if there are unprocessed characters.
    if index < len(prefix):
        raise ValueError("Invalid Prefix Expression: There are too many operands, add an operator.")
    # Validate the constructed tree to ensure every operator has two children.
    tree.isValid()  # This will raise an error if the tree is invalid.
    return tree


def conversion(tree):
    # If tree does not exist, then return whitespace
    if tree is None:
        return ''

    # If tree exists we follow the structure of post-order traversal: left node right node and then root node

    left_node = conversion(tree.left)
    right_node = conversion(tree.right)
    # append and output string following post-order traversal method.
    postfix = left_node + right_node + tree.value

    return postfix