
data = {
    'E': ['TX'],
    'X': ['+TX', 'e'],
    'T': ['FY'],
    'Y': ['*FY', 'e'],
    'F': ['id', '(E)']

}
first = {
    'F': {'id': ['id'], '(E)': ['(']},
    'Y': {'*FY': ['*'], 'e': ['e']},
    'T': {'FY': ['id', '(']},
    'X': {'+TX': ['+'], 'e': ['e']},
    'E': {'TX': ['id', '(']},
}

follow = {
    "E": [')', '$'],
    'X': [')', '$'],
    'T': ['+', ')', '$'],
    'Y': ['+', ')', '$'],
    'F': ['+', '*', ')', '$']
}


def ll1(data, first, follow):
    terminal = []
    l = {}
    for i in first:
        for j in first[i]:
            for k in first[i][j]:
                if k != 'e':
                    l[i, k] = j
                    terminal.append(k)
                else:
                    for a in follow[i]:
                        l[i, a] = j
    for i in follow:
        for j in follow[i]:
            if j != '$':
                terminal.append(j)
    terminal = list(set(terminal))
    key = l.keys()
    terminal = sorted(terminal)
    terminal.append('$')
    
    for i in terminal:
        print("\t\t\t  " + i, end='')
    print("\n", "=" * 80)
    for i in data:
        print(i + "\t\t", end='')
        for j in terminal:
            if ((i, j) in key):
                print(f"| {i}--->{l[i, j]}\t", end='')
            else:
                print("| \t\t\t", end='')

        print("\n", "=" * 80)


ll1(data, first, follow)

'''
This code implements LL(1) parsing table construction algorithm. Let's break it down:

1. **`data`**: Represents the grammar rules where keys are non-terminal symbols and values are lists of production rules associated with each non-terminal.

2. **`first`**: Represents the FIRST sets computed for each non-terminal symbol in the grammar.

3. **`follow`**: Represents the FOLLOW sets computed for each non-terminal symbol in the grammar.

4. **`ll1` function**: This function constructs the LL(1) parsing table using the given grammar data, FIRST sets, and FOLLOW sets.

    - **`terminal`**: Initializes an empty list to store terminal symbols.
    
    - **`l`**: Initializes an empty dictionary to represent the parsing table.
    
    - **Compute Parsing Table**:
    
        - Iterates over each non-terminal symbol `i` in the FIRST set:
        
            - Iterates over each symbol `j` in the FIRST set of `i`:
            
                - If `k` is not epsilon, assigns production `j` to the parsing table entry corresponding to `(i, k)` and adds `k` to the list of terminals.
                
                - If `k` is epsilon, assigns production `j` to the parsing table entry corresponding to `(i, a)` for each symbol `a` in the FOLLOW set of `i`.
                
        - Iterates over each non-terminal symbol `i` in the FOLLOW set:
        
            - Iterates over each symbol `j` in the FOLLOW set of `i`:
            
                - If `j` is not '$', adds `j` to the list of terminals.
                
        - Sorts and appends '$' to the list of terminals to represent the end of input marker.
        
    - **Print Parsing Table**:
    
        - Prints the header row of the parsing table with terminal symbols.
        
        - Iterates over each non-terminal symbol in the grammar:
        
            - Prints the non-terminal symbol.
            
            - Iterates over each terminal symbol:
            
                - If the parsing table entry `(i, j)` exists, prints the production associated with it.
                
                - Otherwise, prints an empty cell.
                
            - Prints a separator row.
            
The function constructs and prints the LL(1) parsing table based on the provided grammar data, FIRST sets, and FOLLOW sets.'''