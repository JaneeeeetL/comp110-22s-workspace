"""Exercise 2!"""
__author__ = str("730401522")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret = str("python")
length_s: int = len(secret)
i_s: int = 0
i_g: int = 0
s: str = ""
guess = str(input(f"What is your {length_s}-letter guess? "))
length_g: int = len(guess)

while length_g != length_s:
    guess = str(input(f"That was not {length_s} letters! Try again: "))
    length_g = len(guess)
while i_g < length_s:
    track: bool = False
    while track is False and i_s < length_s:
        if guess[i_g] == secret[i_s]:
            if i_g == i_s:
                s += GREEN_BOX
            else:
                s += YELLOW_BOX
            track = True
        else:
            i_s += 1
    i_s = 0
    i_g += 1
    if track is False:  
        s += WHITE_BOX
print(s)
if guess == secret:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")