def generate_tac(expression):
    temp_count, code = 0, []
    tokens = tokenize(expression)
    output_queue, operator_stack = [], []

    for token in tokens:
        if token.isalnum():
            output_queue.append(token)
        elif token in {'+', '-', '*', '/', '^'}:
            while operator_stack and has_higher_precedence(operator_stack[-1], token):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop()

    output_queue.extend(reversed(operator_stack))

    operand_stack = []
    for token in output_queue:
        if token.isalnum():
            operand_stack.append(token)
        elif token in {'+', '-', '*', '/', '^'}:
            operand2, operand1 = operand_stack.pop(), operand_stack.pop()
            result_var = f't{temp_count}'
            temp_count += 1
            code.append(f'{result_var} = {operand1} {token} {operand2}')
            operand_stack.append(result_var)
    return code

def tokenize(expression):
    tokens, current_token = [], ''
    for char in expression:
        if char.isalnum():
            current_token += char
        else:
            if current_token:
                tokens.append(current_token)
                current_token = ''
            tokens.append(char)
    if current_token:
        tokens.append(current_token)
    return tokens

def has_higher_precedence(op1, op2):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return precedence.get(op1, 0) >= precedence.get(op2, 0)

# Example usage:
if __name__ == "__main__":
    expression = "a = ( b * c) + 12 * ( e /f ) ^ g"
    tac = generate_tac(expression)
    print("Three Address Code (TAC) for expression:", expression)
    for statement in tac:
        print(statement)

        '''
if __name__ == "__main__":
    expression = input("Enter an arithmetic expression: ")
    tac = generate_tac(expression)
    print("Three Address Code (TAC) for expression:", expression)
    for statement in tac:
        print(statement)
'''

'''
Here's an explanation of the code:

1. **Function Definitions**:
   - `generate_tac(expression)`: This function takes an arithmetic expression as input and generates Three Address Code (TAC) for it.
   - `tokenize(expression)`: This function breaks down the input expression into tokens.
   - `has_higher_precedence(op1, op2)`: This function checks if the precedence of `op1` is higher than or equal to the precedence of `op2`.

2. **Variable Initialization**:
   - `temp_count, code = 0, []`: `temp_count` keeps track of the temporary variable count, and `code` stores the generated TAC instructions.
   - `tokens = tokenize(expression)`: This line tokenizes the input expression using the `tokenize()` function.
   - `output_queue, operator_stack = [], []`: These lists are used to store tokens and operators during the parsing process.

3. **Parsing Tokens**:
   - The `for` loop iterates over each token in the `tokens` list.
   - If the token is an alphanumeric character, it is added to the `output_queue`.
   - If the token is an operator (`+`, `-`, `*`, `/`, `^`), it is pushed onto the `operator_stack`.
   - If the token is an opening parenthesis `(`, it is also pushed onto the `operator_stack`.
   - If the token is a closing parenthesis `)`, all operators on the `operator_stack` are popped and added to the `output_queue` until an opening parenthesis is encountered. Then, the opening parenthesis is popped from the stack.

4. **Generating TAC**:
   - After parsing all tokens, any remaining operators on the `operator_stack` are added to the `output_queue` in reverse order.
   - A new empty stack `operand_stack` is initialized.
   - Another loop iterates over each token in the `output_queue`.
   - If the token is alphanumeric, it is pushed onto the `operand_stack`.
   - If the token is an operator, two operands are popped from the `operand_stack`, and a TAC instruction is generated using the operator, operands, and a temporary variable. This instruction is appended to the `code` list, and the temporary variable is pushed back onto the `operand_stack`.
   - Finally, the generated TAC instructions stored in the `code` list are returned.

5. **Example Usage**:
   - The `generate_tac()` function is called with an example arithmetic expression.
   - The generated TAC instructions are printed to the console.

This code essentially converts an arithmetic expression into Three Address Code (TAC) instructions. It performs tokenization, expression parsing, operator precedence handling, and TAC generation.'''