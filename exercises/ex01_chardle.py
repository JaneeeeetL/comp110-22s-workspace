"""EX01 -- Input, variables, and conditionals."""
__author__ = "730401522"

word: str = input("Enter a 5-character word: ")

if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
else:
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        print("Searching for " + letter + " in " + word)

        instance = 0

        if letter == word[0]:
            print(letter + " found at index 0")
            instance += 1
        if letter == word[1]:
            print(letter + " found at index 1")
            instance += 1
        if letter == word[2]:
            print(letter + " found at index 2")
            instance += 1
        if letter == word[3]:
            print(letter + " found at index 3")
            instance += 1
        if letter == word[4]:
            print(letter + " found at index 4")
            instance += 1
        if instance == 0:
            print("No instances of " + letter + " found in " + word)
        if instance == 1:
            print("1 instance of " + letter + " found in " + word)
        if instance > 1:
            print(str(instance) + " instances of " + letter + " found in " + word)