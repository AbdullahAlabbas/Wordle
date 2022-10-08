class Wordle:

    MAX_ATTEMPS = 6
    WORD_LENGTH = 5
    def __init__(self, secret : str):
        self.secret : str = secret
        self.attemps = []
        pass
        
    def attempt(self, word: str):
        self.attemps.append(word)
    

    @property
    def is_solved(self):
        return len(self.attemps) > 0 and self.attemps[-1] == self.secret

    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPS - len(self.attemps)


    @property
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.is_solved
