def cal_first(s, productions):
    first = set()
    for i in range(len(productions[s])):
        for j in range(len(productions[s][i])):
            c = productions[s][i][j]
            if c.isupper():
                f = cal_first(c, productions)
                if 'ε' not in f:
                    first.update(f)
                    break
                else:
                    if j == len(productions[s][i]) - 1:
                        first.update(f)
                    else:
                        f.remove('ε')
                        first.update(f)
            else:
                first.add(c)
                break
    return first

productions = {
        'S': [['a', 'B', 'D', 'h']],
        'B': [['c', 'C']],
        'C': [['b', 'C'], ['ε']],
        'D': [['E', 'F']],
        'E': [['g'], ['ε']],
        'F': [['f'], ['ε']]
    }
first = {}

for s in productions.keys():
    first[s] = cal_first(s, productions)

print("**FIRST**")
for lhs, rhs in first.items():
    print(lhs, ":", rhs)
    print("")


'''
Sure, let's break down the code line by line:

1. `def cal_first(s, productions):`: This line defines a function named `cal_first` that calculates the FIRST set for a given non-terminal symbol `s` in a given set of productions `productions`.

2. `first = set()`: This line initializes an empty set named `first` to store the FIRST set of the non-terminal symbol `s`.

3. `for i in range(len(productions[s])):`: This line iterates over the productions associated with the non-terminal symbol `s`.

4. `for j in range(len(productions[s][i])):`: This line iterates over the symbols in each production of the non-terminal symbol `s`.

5. `c = productions[s][i][j]`: This line assigns the current symbol being processed to the variable `c`.

6. `if c.isupper():`: This line checks if the current symbol is an uppercase letter, indicating a non-terminal symbol.

7. `f = cal_first(c, productions)`: This line recursively calls the `cal_first` function to compute the FIRST set of the non-terminal symbol `c`.

8. `if 'ε' not in f:`: This line checks if the epsilon symbol ('ε') is not present in the FIRST set of the non-terminal symbol `c`.

9. `first.update(f)`: This line adds the FIRST set of `c` to the FIRST set of the current non-terminal symbol `s`.

10. `break`: This line breaks out of the loop over symbols in the current production since the FIRST set of `c` does not contain epsilon.

11. `else:`: This line indicates that the epsilon symbol ('ε') is present in the FIRST set of the non-terminal symbol `c`.

12. `if j == len(productions[s][i]) - 1:`: This line checks if `c` is the last symbol in the current production.

13. `first.update(f)`: This line adds the FIRST set of `c` to the FIRST set of the current non-terminal symbol `s`.

14. `else:`: This line indicates that `c` is not the last symbol in the current production.

15. `f.remove('ε')`: This line removes the epsilon symbol ('ε') from the FIRST set of `c`.

16. `first.update(f)`: This line adds the modified FIRST set of `c` to the FIRST set of the current non-terminal symbol `s`.

17. `else:`: This line indicates that the current symbol `c` is a terminal symbol.

18. `first.add(c)`: This line adds the terminal symbol `c` to the FIRST set of the current non-terminal symbol `s`.

19. `return first`: This line returns the computed FIRST set for the non-terminal symbol `s`.

20. The rest of the code initializes the `productions` dictionary and then iterates over each non-terminal symbol in the `productions` dictionary to compute and print its FIRST set.'''