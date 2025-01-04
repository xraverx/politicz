# politicz.py
# This revised version implements many of the recommended improvements.
import random
import os
from prettytable import PrettyTable

from dilemmas import dilemmas_data

MAX_TURNS = 25  # Easy tweak if you want more or fewer turns

class Dilemma:
    """
    Represents a single dilemma or event in the game.
    """
    def __init__(self, text, options, effects):
        self.text = text
        self.options = options  # dict { 'a': 'description', 'b': 'description' }
        self.effects = effects  # dict { 'a': {'gdp': 0.2, ...}, 'b': {...} }

class DilemmaManager:
    """
    Manages the pool of dilemmas, ensuring each is presented only once
    until the pool is exhausted. Then re-shuffles if needed (or you can stop).
    """
    def __init__(self, dilemmas_list):
        self.all_dilemmas = [Dilemma(**d) for d in dilemmas_list]
        random.shuffle(self.all_dilemmas)
        self.index = 0

    def get_next_dilemma(self):
        """
        Return the next dilemma from the list, re-shuffling if needed.
        """
        if self.index >= len(self.all_dilemmas):
            # Re-shuffle or handle how you want to proceed when all are used
            random.shuffle(self.all_dilemmas)
            self.index = 0

        dilemma = self.all_dilemmas[self.index]
        self.index += 1
        return dilemma

def clamp(value, min_val=0.0, max_val=1.0):
    """
    Ensures a value stays within [min_val, max_val].
    """
    return max(min_val, min(max_val, value))

class Game:
    VARIABLE_DISPLAY_NAMES = {
        "gdp": "GDP",
        "health": "Health",
        "education": "Education",
        "unemployment": "Unemployment",
        "crime": "Crime",
        "poverty": "Poverty",
        "foreign_relations": "Foreign Relations"
    }

    def __init__(self, difficulty):
        """
        Initialize a new game instance with a given difficulty level.

        :param difficulty: The difficulty level of the game, can be "easy", "normal", or "hard".
        """
        self.difficulty = difficulty
        self.turn = 1
        self.variables = {
            "gdp":             {"easy": 0.8, "normal": 0.5, "hard": 0.2},
            "health":          {"easy": 0.8, "normal": 0.5, "hard": 0.2},
            "education":       {"easy": 0.8, "normal": 0.5, "hard": 0.2},
            "unemployment":    {"easy": 0.2, "normal": 0.5, "hard": 0.8},
            "crime":           {"easy": 0.2, "normal": 0.5, "hard": 0.8},
            "poverty":         {"easy": 0.2, "normal": 0.5, "hard": 0.8},
            "foreign_relations": {"easy": 0.8, "normal": 0.5, "hard": 0.2},
        }

        # Set initial values according to difficulty
        for var in self.variables:
            setattr(self, var, self.variables[var][difficulty])

        # Store initial values for comparison at the end
        self.initial_variables = {
            var: getattr(self, var) for var in self.variables
        }

        # Create a DilemmaManager to manage which dilemmas appear
        self.dilemma_manager = DilemmaManager(dilemmas_data)

    def show_differences(self):
        """
        Prints the difference between the initial and final values of the variables.
        """
        table = PrettyTable()
        table.field_names = ["Variable", "Initial", "Final", "Change"]
        for variable in self.variables:
            display_name = self.VARIABLE_DISPLAY_NAMES.get(variable, variable)
            initial_val = self.initial_variables[variable]
            final_val = getattr(self, variable)
            diff = final_val - initial_val
            table.add_row([
                display_name,
                f"{initial_val:.0%}",
                f"{final_val:.0%}",
                f"{diff:+.0%}"
            ])
        print(table)

    def print_table(self):
        """
        Prints a table showing the current values of the variables.
        """
        print(f"\n=== Turn {self.turn} ===")
        table = PrettyTable()
        table.field_names = ["Variable", "Value"]
        for variable in self.variables:
            display_name = self.VARIABLE_DISPLAY_NAMES.get(variable, variable)
            current_value = getattr(self, variable)
            table.add_row([display_name, f"{current_value:.0%}"])
        print(table)

    def apply_effects(self, effects):
        """
        Apply a dictionary of variable changes. Clamps each variable to [0, 1].
        Returns a dict of {var_name: (old_value, new_value)} for immediate feedback.
        """
        changes = {}
        for var, value in effects.items():
            old_val = getattr(self, var)
            new_val = clamp(old_val + value)
            setattr(self, var, new_val)
            changes[var] = (old_val, new_val)
        return changes

    def show_immediate_feedback(self, changes):
        """
        Shows how each variable changed as a result of the user's choice.
        """
        print("\nEffects of your choice:")
        for var, (old_val, new_val) in changes.items():
            display_name = self.VARIABLE_DISPLAY_NAMES.get(var, var)
            diff = new_val - old_val
            sign = "+" if diff >= 0 else ""
            print(f"  {display_name}: {sign}{diff:.0%}")

    def handle_choice(self, choice, dilemma):
        """
        Handle the user's choice, updating variables and providing feedback.
        """
        choice = choice.lower()
        valid_choices = dilemma.effects.keys()  # typically ['a', 'b']

        if choice not in valid_choices:
            # Let the caller know it's invalid so they can re-prompt
            return False

        # Apply effects
        changes = self.apply_effects(dilemma.effects[choice])
        self.show_immediate_feedback(changes)
        self.turn += 1
        return True

    def present_dilemma(self):
        """
        Presents the next dilemma to the user, and ensures valid input.
        """
        dilemma = self.dilemma_manager.get_next_dilemma()

        # Display text and options
        print("\n" + dilemma.text)
        for key, val in dilemma.options.items():
            print(f"  {key}: {val}")

        # Prompt until valid choice
        while True:
            choice = input("Enter your choice: ").strip().lower()
            if self.handle_choice(choice, dilemma):
                break
            else:
                print("Invalid choice. Please try again.")

    def check_loss(self):
        """
        Check if any of the variables have reached a critical value, indicating a loss in the game.
        Returns True if lost, False otherwise.
        """
        if self.gdp <= 0:
            self.game_over_reason("The country's industries have failed. Economic crisis!")
            return True
        elif self.health <= 0:
            self.game_over_reason("A major health crisis emerged. Many lives lost!")
            return True
        elif self.education <= 0:
            self.game_over_reason("Your education system collapsed!")
            return True
        elif self.unemployment >= 1:
            self.game_over_reason("Widespread unemployment! No jobs left!")
            return True
        elif self.crime >= 1:
            self.game_over_reason("Crime rates skyrocketed. No one feels safe!")
            return True
        elif self.poverty >= 1:
            self.game_over_reason("Poverty reached critical levels!")
            return True
        elif self.foreign_relations <= 0:
            self.game_over_reason("Foreign relations have completely broken down!")
            return True
        return False

    def game_over_reason(self, message):
        """
        Display the final table, differences, and a game over message.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_table()
        print(message, "Game over.")
        self.show_differences()

    def play(self):
        """
        Main game loop, present dilemmas and check for the game's end condition.
        """
        while not self.check_loss() and self.turn <= MAX_TURNS:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.print_table()
            self.present_dilemma()

        if self.turn > MAX_TURNS:
            # Player has survived until the end
            os.system('cls' if os.name == 'nt' else 'clear')
            self.print_table()
            self.show_differences()
            # Example of a simple "multiple endings" check:
            if self.gdp > 0.8 and self.health > 0.8:
                print("Congratulations! You achieved a golden age of prosperity and health!")
            else:
                print("Congratulations! You have s
