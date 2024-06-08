def main():
    prod_rules = []
    final_rules = []

    # with open("/Users/shreyansjain/PycharmProjects/pracs/input.txt", "r") as file:
    #     lines = file.readlines()

    lines = ['t1 = c',
            't2 = a+b',
            't3 = a+b',
            't4 = a+b',
            't5 = a+b',
            't6 = d+5',
            't7 = a+b',
            't8 = c']
            
            
    for line in lines:
        s1 = line.strip()
        print(s1)
        if s1[3:] not in prod_rules:
            prod_rules.append(s1[3:])
            final_rules.append(s1)

    print("printing all production rules")
    # for rule in final_rules:
    #     print(rule)
    for count,rule in enumerate(final_rules):
        print(f"t{count+1}",rule[2:])
main()

'''
Let's go through the code:

1. `def main():`:
   - This line defines a function named `main`.

2. `prod_rules = []`, `final_rules = []`:
   - These lines initialize two empty lists: `prod_rules` and `final_rules`. These lists will store the production rules extracted from the input.

3. `lines = [...]`:
   - This block of code initializes the `lines` list with some example input lines. This is commented out, as the actual input is read from a file in the original code.

4. `for line in lines:`:
   - This line starts a for loop that iterates over each line in the `lines` list.

5. `s1 = line.strip()`:
   - This line removes leading and trailing whitespace from the current line and assigns the result to the variable `s1`.

6. `print(s1)`:
   - This line prints the current line to the console.

7. `if s1[3:] not in prod_rules:`:
   - This line checks if the substring of `s1` starting from index 3 (i.e., after the first three characters) is not already present in the `prod_rules` list.

8. `prod_rules.append(s1[3:])`, `final_rules.append(s1)`:
   - These lines append the substring of `s1` (after the first three characters) to the `prod_rules` list and the entire line `s1` to the `final_rules` list.

9. `print("printing all production rules")`:
   - This line prints a message indicating that all production rules will be printed next.

10. `for count, rule in enumerate(final_rules):`:
    - This line starts a for loop that iterates over each item (rule) in the `final_rules` list, along with its index (`count`).

11. `print(f"t{count+1}", rule[2:])`:
    - This line prints the index (starting from 1) along with the rule extracted from `final_rules`. The index is prefixed with 't'.

The code basically reads input lines, extracts production rules, and prints them with an index prefixed with 't'.'''