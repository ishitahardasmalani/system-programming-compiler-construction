#remove left recursion
def remove_left_recursion(grammar):
    new_grammar = {}

    print("\nOriginal grammar: ")
    for non_terminal , productions in grammar.items():
        print(non_terminal, "->", "|".join(productions))

        alpha_productions = []
        beta_productions = []

        for production in productions:
            if(production[0]==non_terminal):
                alpha_productions.append(production[1:])
            else:
                beta_productions.append(production)

        if alpha_productions:
            non_terminal_dash = non_terminal + "'"
            new_grammar[non_terminal] = [beta + non_terminal_dash for beta in beta_productions]
            new_grammar[non_terminal_dash] = [alpha + non_terminal_dash if alpha else '#' for alpha in alpha_productions] + ['#']
        else:
            new_grammar[non_terminal]=productions
    print("\nGrammar after Eliminating Left Recursion: ")
    for non_terminal,productions in new_grammar.items():
        print(non_terminal,"->","|".join(productions))
    return new_grammar

original_grammar={
    'S': ['A'],
    'A': ['Ad','Ae','aB','ac'],
    'B': ['bBc','f']
}

modified_grammar = remove_left_recursion(original_grammar)

'''
Sure, let's go through the code line by line:

1. `def remove_left_recursion(grammar):`:
   - This line defines a function named `remove_left_recursion` that takes a dictionary `grammar` as input. This function is intended to remove left recursion from the given context-free grammar.

2. `new_grammar = {}`:
   - This line initializes an empty dictionary `new_grammar`. This dictionary will store the modified grammar after removing left recursion.

3. `print("\nOriginal grammar: ")`:
   - This line prints a message indicating that the original grammar is going to be displayed.

4. `for non_terminal, productions in grammar.items():`:
   - This line starts a loop over each key-value pair in the `grammar` dictionary. Each key represents a non-terminal symbol, and the corresponding value is a list of production rules for that non-terminal.

5. `print(f"{non_terminal} -> {' | '.join(productions)}")`:
   - This line prints each non-terminal symbol along with its production rules. It formats the output to display the productions separated by `|`.

6. `alpha_productions = []`:
   - This line initializes an empty list `alpha_productions`. It will store the production rules with left recursion.

7. `beta_productions = []`:
   - This line initializes an empty list `beta_productions`. It will store the production rules without left recursion.

8. `for production in productions:`:
   - This line starts a loop over each production rule for the current non-terminal symbol.

9. `if production.startswith(non_terminal):`:
   - This line checks if the current production rule starts with the same non-terminal symbol. If it does, it indicates left recursion.

10. `alpha_productions.append(production[1:])`:
    - This line appends the production rule excluding the first character (the non-terminal symbol) to the `alpha_productions` list.

11. `else:`:
    - This line executes if the current production rule does not start with the same non-terminal symbol.

12. `beta_productions.append(production)`:
    - This line appends the current production rule to the `beta_productions` list, as it does not exhibit left recursion.

13. `if alpha_productions:`:
    - This line checks if there are any production rules with left recursion (`alpha_productions` is not empty).

14. `non_terminal_dash = non_terminal + "'"`:
    - This line creates a new non-terminal symbol by appending a prime symbol `'` to the original non-terminal symbol.

15. `new_grammar[non_terminal] = [f"{beta}{non_terminal_dash}" for beta in beta_productions]`:
    - This line creates new production rules for the original non-terminal symbol without left recursion by appending the prime symbol to each beta production.

16. `new_grammar[non_terminal_dash] = [f"{alpha}{non_terminal_dash}" if alpha else '#' for alpha in alpha_productions] + ['#']`:
    - This line creates new production rules for the non-terminal symbol with left recursion by appending the prime symbol to each alpha production. It also adds an empty string `'#'` to indicate epsilon production.

17. `else:`:
    - This line executes if there are no production rules with left recursion for the current non-terminal symbol.

18. `new_grammar[non_terminal] = productions`:
    - This line assigns the original production rules to the non-terminal symbol in the modified grammar.

19. `print("\nGrammar after Eliminating Left Recursion: ")`:
    - This line prints a message indicating that the grammar after removing left recursion is going to be displayed.

20. `for non_terminal, productions in new_grammar.items():`:
    - This line starts a loop over each key-value pair in the `new_grammar` dictionary, representing the modified grammar.

21. `print(f"{non_terminal} -> {' | '.join(productions)}")`:
    - This line prints each non-terminal symbol along with its modified production rules. It formats the output to display the productions separated by `|`.

22. `return new_grammar`:
    - This line returns the modified grammar stored in the `new_grammar` dictionary.'''