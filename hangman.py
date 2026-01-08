"""
Hangman Game - Algorithm Design Implementation
Demonstrates string manipulation, set operations, and game logic algorithms
"""

import random

class HangmanGame:
    """
    Hangman game class demonstrating algorithmic concepts:
    - String processing and manipulation
    - Set operations for tracking guessed letters
    - Game state management
    - Input validation algorithms
    """

    def __init__(self, word_list=None):
        """Initialize game with word list. O(1) time complexity."""
        if word_list is None:
            word_list = [
              "MESSI", "RONALDO", "NEYMAR", "MBAPPE",
"MARADONA", "PELE", "ZIDANE", "BECKHAM",
"RONALDINHO", "LEWANDOWSKI", "SALAH", "HAZARD",
"INIESTA", "XAVI", "BUFFON", "MODRIC",
"KANE", "HAALAND", "ROONEY", "HENRY",
"RIVALDO", "TOTTI", "PIRLO", "DROGBA",
"SUAREZ", "VANPERSIE", "ROBBEN", "SCHWEINSTEIGER",
"GERRARD", "LAMPARD", "VIDIC", "PUYOL",
"SERGIORAMOS", "CASILLAS", "COURTOIS", "DEBRUYNE",
"GRIEZMANN", "POGBA", "DYBALA",
"BARCELONA", "REALMADRID", "MANCHESTERUNITED", "LIVERPOOL",
"BAYERNMUNICH", "JUVENTUS", "PSG", "ACMILAN",
"INTERMILAN", "CHELSEA", "ARSENAL", "ATLETICOMADRID",
"SEVILLA", "AJAX", "BENFICA", "PORTO",
"GALATASARAY", "FENERBAHCE", "BESIKTAS",
"WORLDCUP", "CHAMPIONSLEAGUE", "BALLONDOR", "GOLDENBOOT",
"FIFA", "UEFA", "COPAAMERICA", "EUROCUP",
"LALIGA", "PREMIERLEAGUE", "SERIEA", "BUNDESLIGA",
"ELCLASICO", "SUPERCUP", "CLUBWORLDCUP", "NATIONSLEAGUE",
"AFRICANCUP",
"WEMBLEY", "CAMPNOU", "SANTIAGOBERNABEU", "OLDTRAFFORD",
"ANFIELD", "MARACANA", "ALLIANZARENA", "SIGNALIDUNAPARK",
"ETIHADSTADIUM", "EMIRATESSTADIUM",
"PUSKASAWARD", "BESTFIFA", "TEAMOFYEAR", "TRANSFERMARKET",
"DEADLINEDAY", "HATTRICK", "FREEKICK", "PENALTYSHOOTOUT",
"VAR", "OFFSIDE", "TIKIATAKA"]
        self.word_list = word_list
        self.max_attempts = 6
        self.reset_game()

    def reset_game(self):
        """Reset game state. O(1) time complexity."""
        self.secret_word = random.choice(self.word_list).upper()
        self.guessed_letters = set()  # O(1) membership checks
        self.attempts_left = self.max_attempts
        self.game_over = False
        self.won = False

    def get_display_word(self):
        """
        Generate word display with blanks and guessed letters.
        Algorithm: Linear scan O(n) where n = word length
        """
        display = []
        for letter in self.secret_word:
            if letter in self.guessed_letters:  # O(1) set lookup
                display.append(letter)
            else:
                display.append("_")
        return " ".join(display)

    def make_guess(self, guess):
        """
        Process player guess with validation.
        Returns: (is_correct, message, status_code)
        """
        if self.game_over:
            return False, "Game over!", "finished"

        guess = guess.upper().strip()

        # Input validation algorithm
        if len(guess) != 1 or not guess.isalpha():
            return False, "Enter single letter only!", "invalid"

        if guess in self.guessed_letters:  # O(1) check
            return False, f"'{guess}' already guessed!", "duplicate"

        self.guessed_letters.add(guess)  # O(1) add

        if guess in self.secret_word:  # O(n) string search
            if self._check_win_condition():  # O(n) check
                self.game_over = True
                self.won = True
                return True, f"Yes! Word: {self.secret_word}", "won"
            return True, f"Good! '{guess}' found", "correct"
        else:
            self.attempts_left -= 1
            if self.attempts_left == 0:
                self.game_over = True
                return False, f"No! Word was: {self.secret_word}", "lost"
            return False, f"Wrong! {self.attempts_left} tries left", "incorrect"

    def _check_win_condition(self):
        """Check if all letters guessed. O(n) set operations."""
        word_letters = set(self.secret_word)  # O(n)
        return word_letters.issubset(self.guessed_letters)  # O(n)

    def get_game_state(self):
        """Return current game information."""
        return {
            "word_display": self.get_display_word(),
            "attempts": self.attempts_left,
            "guessed": sorted(list(self.guessed_letters)),
            "game_over": self.game_over,
            "won": self.won
        }


def draw_hangman(attempts_left):
    """ASCII art for hangman - visual feedback algorithm."""
    stages = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    return stages[6 - attempts_left]


def play_hangman():
    """Main game loop with user interaction."""
    game = HangmanGame()

    print("🎯 HANGMAN GAME 🎯")
    print("Guess the programming word!")
    print(f"You have {game.max_attempts} attempts.\n")

    while not game.game_over:
        state = game.get_game_state()

        print(draw_hangman(state["attempts"]))
        print(f"Word: {state['word_display']}")
        print(f"Tries left: {state['attempts']}")
        print(f"Guessed: {', '.join(state['guessed'])}\n")

        try:
            guess = input("Guess a letter: ").strip()
            if not guess:
                print("Please enter a letter!\n")
                continue

            correct, message, status = game.make_guess(guess)
            print(message)

            if status in ["won", "lost"]:
                print("\n" + "="*30)
                if status == "won":
                    print("🎉 CONGRATULATIONS! You won! 🎉")
                else:
                    print("💀 GAME OVER! Better luck next time!")
                print("="*30)

        except KeyboardInterrupt:
            print("\n\nGame interrupted. Thanks for playing!")
            return

    # Play again option
    while True:
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again == 'y':
            print("\n" + "="*40)
            play_hangman()
            return
        elif again == 'n':
            print("Thanks for playing Hangman!")
            return
        else:
            print("Please enter 'y' or 'n'")


def algorithm_demo():
    """Demonstrate the algorithms used in Hangman."""
    print("🔍 HANGMAN ALGORITHM ANALYSIS 🔍")
    print("=" * 50)

    game = HangmanGame(["ALGORITHM"])

    print(f"Secret word: {game.secret_word}")
    print(f"Initial state: {game.get_display_word()}")

    # Simulate gameplay
    guesses = ["A", "L", "G", "O", "R", "I", "T", "H", "M"]

    for i, guess in enumerate(guesses, 1):
        print(f"\n--- Turn {i} ---")
        print(f"Guessing: {guess}")

        correct, message, status = game.make_guess(guess)
        state = game.get_game_state()

        print(f"Result: {message}")
        print(f"Display: {state['word_display']}")
        print(f"Guessed letters: {state['guessed']}")
        print(f"Status: {status}")

        if game.game_over:
            break

    print("\n📊 ALGORITHM COMPLEXITIES:")
    print("- Word display generation: O(n)")
    print("- Guess validation: O(1) set operations")
    print("- Win condition check: O(n) set comparison")
    print("- Overall per guess: O(n)")
    print("- Space complexity: O(n) for guessed letters set")


if __name__ == "__main__":
    print("Choose mode:")
    print("1. Play Hangman Game")
    print("2. Algorithm Demonstration")

    choice = input("Enter choice (1 or 2): ").strip()

    if choice == "2":
        algorithm_demo()
    else:
        play_hangman()
