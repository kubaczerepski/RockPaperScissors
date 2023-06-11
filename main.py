import random

class Game:
    def __init__(self):
        self._choices = ["kamień", "papier", "nożyce"]
        self._player_choice = None
        self._computer_choice = None
        self._player_wins = 0
        self._computer_wins = 0

    def get_player_choice(self):
        return self._player_choice

    def set_player_choice(self, value):
        if value.lower() in self._choices:
            self._player_choice = value.lower()
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

    def generate_computer_choice(self):
        self._computer_choice = random.choice(self._choices)

    def compare_choices(self):
        if self._player_choice == self._computer_choice:
            return "Remis"
        elif (
                (self._player_choice == "kamień" and self._computer_choice == "nożyce") or
                (self._player_choice == "papier" and self._computer_choice == "kamień") or
                (self._player_choice == "nożyce" and self._computer_choice == "papier")
        ):
            self._player_wins += 1
            return "Gratulacje, wygrałeś!"
        else:
            self._computer_wins += 1
            return "Niestety, przegrałeś!"

    def start(self):
        print("Witaj! Zagrajmy w Kamień, Papier, Nożyce.")

        while True:
            print(f"\nWygrane: Gracz - {self._player_wins}, Komputer - {self._computer_wins}\n")
            player_choice = input("Wybierz swoją opcję (kamień, papier, nożyce): ")
            self.set_player_choice(player_choice)

            if self.get_player_choice() is None:
                continue

            self.generate_computer_choice()

            print(f"Komputer wybrał: {self._computer_choice}")
            result = self.compare_choices()
            print(result)

            play_again = input("Czy chcesz zagrać ponownie? (tak/nie): ")
            if play_again.lower() != "tak":
                break

class RockPaperScissors(Game):
    def compare_choices(self):
        if self.get_player_choice() == self._computer_choice:
            return "Remis"
        elif (
                (self.get_player_choice() == "kamień" and self._computer_choice == "nożyce") or
                (self.get_player_choice() == "papier" and self._computer_choice == "kamień") or
                (self.get_player_choice() == "nożyce" and self._computer_choice == "papier")
        ):
            self._player_wins += 1
            return "Gratulacje, wygrałeś!"
        else:
            self._computer_wins += 1
            return "Niestety, przegrałeś!"

game = RockPaperScissors()
game.start()

