__author__ = str("730401522")


def contains_char(s1: str, s2: str) -> bool:
    """A function to search for character at any index."""
    assert len(s2) == 1
    s1_i: int = 0
    while s1_i < len(s1):
        if s1[s1_i] == s2:
            return True
        else: 
            s1_i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """A function to print emojis."""
    assert len(guess) == len(secret)
    i_g: int = 0
    i_s: int = 0
    s: str = ""
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    WHITE_BOX: str = "\U00002B1C"
    while i_g < len(secret):
        test: bool = contains_char(secret, guess[i_g])
        if test is True and guess[i_g] == secret[i_s]:
            s += GREEN_BOX
        elif test is True:
            s += YELLOW_BOX
        else:
            s += WHITE_BOX
        i_g += 1
        i_s += 1
    return s
        
    
def input_guess(n: int) -> str:
    length: str = input(f"Enter a {n} character word: ")
    while len(length) != n:
        length: str = input(f"That wasn't {n} chars! Try again: ")
    return length
    

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    won: bool = False
    n: int = 5
    secret: str = "codes"
    while turns <= 6 and won is False:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(n)
        print(emojified(guess, secret))
        if guess == secret:
            won = True
            print(f"You won in {turns}/6 turns!")
        turns += 1
    if turns > 6 and won is False:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()