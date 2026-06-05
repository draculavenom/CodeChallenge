letterOptions = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

positions = [0, 0, 0, 0, 0]

password = "zzzzz"#input("insert the password: ")
password = password.upper()

while positions != [len(letterOptions) - 1, len(letterOptions) - 1, len(letterOptions) - 1, len(letterOptions) - 1, len(letterOptions) - 1]:
    if password == letterOptions[positions[4]] + letterOptions[positions[3]] + letterOptions[positions[2]] + letterOptions[positions[1]] + letterOptions[positions[0]]:
        print("the password is: " + letterOptions[positions[4]] + letterOptions[positions[3]] + letterOptions[positions[2]] + letterOptions[positions[1]] + letterOptions[positions[0]])
        exit()
    #print(letterOptions[positions[4]] + letterOptions[positions[3]] + letterOptions[positions[2]] + letterOptions[positions[1]] + letterOptions[positions[0]])
    i = 0
    positions[i] = positions[i] + 1
    while positions[i] >= len(letterOptions):
        positions[i] = 0
        i = i + 1
        if i >= len(positions):
            break
        positions[i] = positions[i] + 1
    

if password == letterOptions[positions[4]] + letterOptions[positions[3]] + letterOptions[positions[2]] + letterOptions[positions[1]] + letterOptions[positions[0]]:
    print("the password is: " + letterOptions[positions[4]] + letterOptions[positions[3]] + letterOptions[positions[2]] + letterOptions[positions[1]] + letterOptions[positions[0]])
    exit()