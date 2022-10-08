from WORDLE.wordle import Wordle

def main():
    print("Hello Wordle!")
    wordle = Wordle("APPLE")

    while wordle.can_attempt:
        x = input("Type your guess: ")
        wordle.attempt(x)

    if wordle.is_solved:
        print("You've solved the puzzle.")
    else:
        print("You Failed to solved the puzzele!")
        

if __name__ == "__main__":
    main()