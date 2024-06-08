import re

tokens = []
commands = input("Enter a command:")
sourceCode = commands.split()

for word in sourceCode:
    if word in ['str', 'int', 'bool', 'if', 'else', 'do', 'while', 'elif', 'in', 'range', 'for', 'switch', 'case', 'break']:
        tokens.append(['Keyword', word])
    elif re.match("[a-zA-Z_][a-zA-Z0-9_]*$", word):
        tokens.append(['Identifier', word])
    elif word in "+-*/%=;":
        tokens.append(['Operator', word])
    elif re.match("\d+\.\d+", word):
        tokens.append(["Float", word])  
    elif re.match("\d+", word):
        tokens.append(["Integer", word])
    elif word in [':', ';']:
        tokens.append(["Separator", word])  
    else:
        tokens.append(["String", word])

print(tokens)