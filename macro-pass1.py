with open("/Users/shreyansjain/PycharmProjects/pracs/File1.txt", "r") as file:
    lines = file.readlines()

mnt = []
mdt = []
ala = []

i = 0

while i < len(lines):
    line = lines[i].strip().upper()
    if line == "MACRO":
        counter = 0
        i += 1
        while lines[i].strip().upper() != "MEND":
            if counter == 0:
                mac = lines[i].strip().split(' ')
                if mac[0] not in ala:
                    ala.append(mac[0])
                temp_ind = ala.index(mac[0])
                mdt.append(mac)
                mdtIndex = len(mdt)
                mnt.append([mac[1], str(mdtIndex)])

                for arg in mac[2].split(','):
                    arg_name = arg.split('=')[0]
                    if arg_name not in ala:
                        ala.append(arg_name)
                counter += 1
                i += 1
            else:
                mac = lines[i].strip().split(' ')
                if len(mac) == 2:
                    arg_index = ala.index(mac[1].split(',')[1])
                    mdt.append(['', mac[0], f"{mac[1].split(',')[0]}," + "#" + str(arg_index)])
                elif len(mac) == 3:
                    arg_index = ala.index(mac[2].split(',')[1])
                    temp_index = ala.index(mac[0])
                    mdt.append([f'#{temp_index}', mac[1], f"{mac[2].split(',')[0]}," + "#" + str(arg_index)])
                i += 1
    else:
        if line == "MEND":
            mdt.append(['', "MEND", ''])
        i += 1

print("\nMNT")
print("Index\tName\tMDT index")
for count, itr in enumerate(mnt):
    print(f"{count + 1}\t{itr[0]}\t{itr[1]}")

print("\nMDT")
print("Index\t\tName")
for count, itr in enumerate(mdt):
    print(f"{count + 1}\t{itr[0]}\t{itr[1]}\t{itr[2]}")

print("\nDummy ALA in Pass 1")
print("Index\tArguments")
for count, itr in enumerate(ala):
    print(f"{count}\t{itr}")

'''
//mac.txt
PRG START 0
MACRO
&LAB INCR &ARG1,&ARG2,&ARG3
&LAB A 1,&ARG1
A 2,&ARG2
A 3,&ARG3
MEND
MACRO
&LAB SUB &ARG4,&ARG5,&ARG6
&LAB A 1,&ARG4
A 2,&ARG5
A 3,&ARG6
MEND
LOOP1 INCR DATA1,DATA2,DATA3
DATA1 DC F’5’
DATA2 DC F’10’
DATA3 DC F’15’

'''

'''
# with open("/Users/shreyansjain/PycharmProjects/pracs/File1.txt", "r") as file:
#     lines = file.readlines()

lines=['PRG START 0',
    'MACRO',
    '&LAB INCR &ARG1,&ARG2,&ARG3',
    '&LAB A 1,&ARG1',
    'A 2,&ARG2',
    'A 3,&ARG3',
    'MEND',
    'MACRO',
    '&LAB SUB &ARG4,&ARG5,&ARG6',
    '&LAB A 1,&ARG4',
    'A 2,&ARG5',
    'A 3,&ARG6',
    'MEND',
    'LOOP1 INCR DATA1,DATA2,DATA3',
    'DATA1 DC F’5’',
    'DATA2 DC F’10’',
    'DATA3 DC F’15’']

mnt = []
mdt = []
ala = []

i = 0

while i < len(lines):
    line = lines[i].strip().upper()
    if line == "MACRO":
        counter = 0
        i += 1
        while lines[i].strip().upper() != "MEND":
            if counter == 0:
                mac = lines[i].strip().split(' ')
                if mac[0] not in ala:
                    ala.append(mac[0])
                temp_ind = ala.index(mac[0])
                mdt.append(mac)
                mdtIndex = len(mdt)
                mnt.append([mac[1], str(mdtIndex)])

                for arg in mac[2].split(','):
                    arg_name = arg.split('=')[0]
                    if arg_name not in ala:
                        ala.append(arg_name)
                counter += 1
                i += 1
            else:
                mac = lines[i].strip().split(' ')
                if len(mac) == 2:
                    arg_index = ala.index(mac[1].split(',')[1])
                    mdt.append(['', mac[0], f"{mac[1].split(',')[0]}," + "#" + str(arg_index)])
                elif len(mac) == 3:
                    arg_index = ala.index(mac[2].split(',')[1])
                    temp_index = ala.index(mac[0])
                    mdt.append([f'#{temp_index}', mac[1], f"{mac[2].split(',')[0]}," + "#" + str(arg_index)])
                i += 1
    else:
        if line == "MEND":
            mdt.append(['', "MEND", ''])
        i += 1

print("\nMNT")
print("Index\tName\tMDT index")
for count, itr in enumerate(mnt):
    print(f"{count + 1}\t{itr[0]}\t{itr[1]}")

print("\nMDT")
print("Index\t\tName")
for count, itr in enumerate(mdt):
    print(f"{count + 1}\t{itr[0]}\t{itr[1]}\t{itr[2]}")

print("\nDummy ALA in Pass 1")
print("Index\tArguments")
for count, itr in enumerate(ala):
    print(f"{count}\t\t{itr}")

'''

'''
Let's break down the code line by line:

1. `with open("/Users/shreyansjain/PycharmProjects/pracs/File1.txt", "r") as file:`:
   - This line opens a file named "File1.txt" in read mode. The file path indicates the location of the file on the system.

2. `lines = file.readlines()`:
   - This line reads all lines from the file and stores them as a list of strings in the variable `lines`.

3. `mnt = []`, `mdt = []`, `ala = []`:
   - These lines initialize three empty lists: `mnt` (Macro Name Table), `mdt` (Macro Definition Table), and `ala` (Argument List Array).

4. `i = 0`:
   - This line initializes a variable `i` to 0, which will be used as an index to iterate over the lines.

5. `while i < len(lines):`:
   - This line starts a while loop that iterates over each line in the file until `i` reaches the length of the `lines` list.

6. `line = lines[i].strip().upper()`:
   - This line retrieves the current line from the `lines` list, removes leading and trailing whitespace using `strip()`, and converts the line to uppercase using `upper()`. It stores the result in the variable `line`.

7. `if line == "MACRO":`:
   - This line checks if the current line is equal to "MACRO".

8. `counter = 0`:
   - This line initializes a counter variable to 0. It will be used to differentiate between different parts of the macro definition.

9. `while lines[i].strip().upper() != "MEND":`:
   - This line starts a nested while loop that continues until "MEND" is encountered, indicating the end of the macro definition.

10. `if counter == 0:`:
    - This line checks if the counter is 0, indicating the first line of the macro definition.

11. `mac = lines[i].strip().split(' ')`:
    - This line splits the current line into a list of strings using space (' ') as the delimiter and removes leading and trailing whitespace. It stores the result in the variable `mac`.

12. `if mac[0] not in ala:`:
    - This line checks if the first element of the `mac` list (the macro name) is not already present in the `ala` list (Argument List Array).

13. `temp_ind = ala.index(mac[0])`:
    - This line retrieves the index of the macro name in the `ala` list and stores it in the variable `temp_ind`.

14. `mdt.append(mac)`:
    - This line appends the current macro definition (represented as a list `mac`) to the `mdt` list (Macro Definition Table).

15. `mdtIndex = len(mdt)`:
    - This line calculates the index of the current macro definition in the `mdt` list and stores it in the variable `mdtIndex`.

16. `mnt.append([mac[1], str(mdtIndex)])`:
    - This line appends a new entry to the `mnt` list (Macro Name Table). The entry consists of the macro name (`mac[1]`) and the index of the macro definition in the `mdt` list (converted to a string).

The explanation continues in the next message due to length limitations.
'''