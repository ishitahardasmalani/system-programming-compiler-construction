data = {
   "S":['aBDh'],
   'B':['cC'],
   'C':['bC','e'],
   'D':['EF'],
   'E':['g','e'],
   'F':['f','e']
}

first = {
   "S":['a'],
   'B':['c'],
   'C':['b','e'],
   'D':['g','f','e'],
   'E':['g','e'],
   'F':['f','e']
}
opp={}
follow = {}

# data = {
#     'S': ['TE'],
#     'E': ['+TE', 'e'],
#     'T': ['FY'],
#     'Y': ['*FY', 'e'],
#     'F': ['(S)', 'id']
# }
# first = {
#     'F': ['(', 'i'],
#     'Y': ['*', 'e'],
#     'T': ['(', 'i'],
#     'E': ['+', 'e'],
#     'S': ['(', 'i']
# }
# opp = ['(', ')', '+', '*', '-']


def fol(i, follow):
    temp = []
    if i == "S":
        temp.append("$")
    for j in data:
        for k in data[j]:
            Index = k.find(i)
            if Index == -1:
                continue
            p = Index + 1
            if p != len(k):
                if k[p].islower() or k[p] in opp:
                    temp.append(k[p])
                else:
                    for u in first[k[p]]:
                        if 'e' != u:
                            temp.append(u)
                    for u in fol(k[p], follow):
                        temp.append(u)
            else:
                if i != j:
                    for o in follow[j]:
                        if o != 'e':
                            temp.append(o)

    return temp


for i in data:
    temp = fol(i, follow)
    follow[i] = list(set(temp))

print("Follow : ")
print(follow)

'''
This code seems to be computing the FOLLOW sets for each non-terminal symbol in a given context-free grammar. Let's break it down:

1. `data`: This dictionary represents the productions of the grammar, where keys are non-terminal symbols and values are lists of production rules associated with each non-terminal.

2. `first`: This dictionary represents the FIRST sets computed for each non-terminal symbol in the grammar.

3. `opp`: This variable seems to represent the operators used in the grammar, but it is currently empty.

4. `follow`: This dictionary will store the FOLLOW sets for each non-terminal symbol.

5. `def fol(i, follow)`: This defines a function `fol` that computes the FOLLOW set for a given non-terminal symbol `i` and updates the `follow` dictionary.

6. `temp = []`: Initializes an empty list `temp` to store the FOLLOW set for the non-terminal symbol `i`.

7. `if i == "S":`: Checks if the current non-terminal symbol is the start symbol 'S'. If so, appends the end of input marker '$' to its FOLLOW set.

8. `for j in data:`: Iterates over each non-terminal symbol in the grammar.

9. `for k in data[j]:`: Iterates over each production rule associated with the non-terminal symbol `j`.

10. `Index = k.find(i)`: Finds the index of the current non-terminal symbol `i` in the production rule `k`.

11. `if Index == -1:`: If the current non-terminal symbol is not found in the production rule, continue to the next rule.

12. `p = Index + 1`: Gets the index of the symbol immediately following the current non-terminal symbol `i`.

13. `if p != len(k):`: Checks if the current non-terminal symbol `i` is not the last symbol in the production rule `k`.

14. `if k[p].islower() or k[p] in opp:`: Checks if the symbol following `i` is a lowercase letter or an operator.

15. `temp.append(k[p])`: Appends the symbol following `i` to the FOLLOW set of `i`.

16. `else:`: If the symbol following `i` is a non-terminal symbol.

17. `for u in first[k[p]]:`: Iterates over the FIRST set of the symbol following `i`.

18. `if 'e' != u:`: If the FIRST set contains symbols other than epsilon, appends them to the FOLLOW set of `i`.

19. `for u in fol(k[p], follow):`: Recursively computes the FOLLOW set of the symbol following `i`.

20. `temp.append(u)`: Appends the computed FOLLOW set to the FOLLOW set of `i`.

21. `else:`: If `i` is the last symbol in the production rule `k`.

22. `if i != j:`: Checks if `i` is not the same as `j`.

23. `for o in follow[j]:`: Appends the FOLLOW set of `j` to the FOLLOW set of `i`.

24. `return temp`: Returns the computed FOLLOW set for the non-terminal symbol `i`.

25. The code then iterates over each non-terminal symbol in `data` and computes its FOLLOW set using the `fol` function, storing the results in the `follow` dictionary.

26. Finally, it prints the computed FOLLOW sets.'''