asciiNumber = 65
for i in range(0, 7):
    for j in range(0, i + 2):
        character = chr(asciiNumber)
        print(character, end=' ')
        asciiNumber +=1
    print(" ")