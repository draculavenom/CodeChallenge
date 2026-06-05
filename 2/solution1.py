print("brute force solution with 5 fors")

letterOptions = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

password = input("insert the password: ")
password = password.upper()

for i in range(len(letterOptions)):
    for j in range(len(letterOptions)):
        for k in range(len(letterOptions)):
            for l in range(len(letterOptions)):
                for m in range(len(letterOptions)):
                    if password == letterOptions[i] + letterOptions[j] + letterOptions[k] + letterOptions[l] + letterOptions[m]:
                        print("the password is: " + letterOptions[i] + letterOptions[j] + letterOptions[k] + letterOptions[l] + letterOptions[m])
                        exit()
