# This code defines a class called "Game" that simulates a game in which the user makes decisions and the values of certain variables (GDP, health, education, unemployment, crime, poverty, and foreign relations) change as a result. The class provides methods to present dilemmas, handle user's choices, print the current variables' state, and check the game's end condition.

import random
import os
from prettytable import PrettyTable
from dilemmas import dilemmas

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
    """
    A dictionary that maps the variable names to their display names.
    """

    def __init__(self, difficulty):
        """
        Initialize a new game instance with a given difficulty level.

        :param difficulty: The difficulty level of the game, it can be "easy", "normal", or "hard".
        """
        self.difficulty = difficulty
        self.turn = 1
        self.variables = {
            "gdp": {"easy": 0.8, "normal": 0.5, "hard": 0.2},
            "health": {"easy": 0.8, "normal": 0.5, "hard": 0.2},
            "education": {"easy": 0.8, "normal": 0.5, "hard": 0.2},
            "unemployment": {"easy": 0.2, "normal": 0.5, "hard": 0.8},
            "crime": {"easy": 0.2, "normal": 0.5, "hard": 0.8},
            "poverty": {"easy": 0.2, "normal": 0.5, "hard": 0.8},
            "foreign_relations": {"easy": 0.8, "normal": 0.5, "hard": 0.2},
        }
        self.initial_variables = {}  # new dictionary to store initial variables
        for variable in self.variables:
            setattr(self, variable, self.variables[variable][difficulty])
            self.initial_variables[variable] = self.variables[variable][difficulty]  # storing initial variables

    def show_differences(self):
        """
        Prints the difference between the initial and final values of the variables
        """
        table = PrettyTable()
        table.field_names = ["Variable", "Changes"]
        for variable in self.variables:
            display_name = self.VARIABLE_DISPLAY_NAMES.get(variable, variable)
            difference = round(getattr(self, variable) - self.initial_variables[variable], 1)
            table.add_row([display_name, difference])
        print(table)

    def handle_choice(self, choice, effects):
        """
        Handle the user's choice and updates the variables accordingly.

        :param choice: The user's choice (a string)
        :param effects: A dictionary containing the effects of each choice on the variables
        """
        if choice not in effects:
            print("Invalid choice. Please try again.")
            return

        for var, value in effects[choice].items():
            setattr(self, var, min(1.01, max(-0.01, getattr(self, var) + value)))
        self.turn += 1
        self.print_table()

    def print_table(self):
        """
        Prints a table showing the current values of the variables
        """
        print("Turn: ", self.turn)
        table = PrettyTable()
        table.field_names = ["Variable", "Value"]
        for variable in self.variables:
            display_name = self.VARIABLE_DISPLAY_NAMES.get(variable, variable)
            table.add_row([display_name, round(getattr(self, variable), 1)])
        print(table)

    def present_dilemma(self):
        """
        Presents a random dilemma to the user, displaying the options and waits for the user's choice
        """
        current_dilemma = random.choice(dilemmas)
        print(current_dilemma["text"])
        options = current_dilemma["options"]
        for key, value in options.items():
            print(f"{key}: {value}")
        choice = input("Enter your choice: ")
        self.handle_choice(choice, current_dilemma["effects"])
    def check_loss(self):
        """
        Check if any of the variables have reached a critical value, indicating a loss in the game.
        """
        if self.gdp <= 0:
            print("The country's industries and businesses are failing, resulting in a widespread economic crisis. Game over.")
            self.show_differences()  # calling the method to show the differences
            return True
        elif self.health <= 0:
            print("A major health crisis has emerged and your government's response has been inadequate. Many lives have been lost. Game over.")
            self.show_differences()  # calling the method to show the differences
            return True
        elif self.education <= 0:
            print("Your country's education system is in a state of disrepair. The youth of your nation are not receiving the education they need. Game over.")
            self.show_differences()  # calling the method to show the differences
            return True
        elif self.unemployment >= 1:
            print("Your government's economic policies have led to widespread unemployment. Game over.")
            self.show_differences()  # calling the method to show the differences
            return True
        elif self.crime >= 1:
            print("Crime rates in your country have skyrocketed, and the citizens no longer feel safe. Game over.")
            self.show_differences()  # calling the method to show the differences
            return True
        elif self.poverty >= 1:
            print("Poverty levels in your country are at an all-time high. Game over.")
            self.show_differences()  # calling the method to show the differences
            return True
        elif self.foreign_relations <= 0:
            print("Your country's foreign relations have completely broken down. Game over.")
            self.show_differences()  # calling the method to show the differences
            return True
        else:
            return False

    def play(self):
        """
        Main game loop, present dilemmas and check for the game's end condition until the game is over.
        """
        while not self.check_loss() and self.turn < 25:
            os.system('cls' if os.name == 'nt' else 'clear') # this line clears the console for better visualization
            self.print_table()
            current_dilemma = random.choice(dilemmas)
            print(current_dilemma["text"])
            options = current_dilemma["options"]
            for key, value in options.items():
                print(f"{key}: {value}")
            choice = input("Enter your choice: ")
            self.handle_choice(choice, current_dilemma["effects"])
        if self.turn >=25:
            self.show_differences()  # calling the method to show the differences
            print("Congratulations! You have won the game.")

# Main function
def main():
    difficulty = input("Choose a difficulty level (easy = 1, normal = 2, hard = 3): ")
    difficulty_mapping = {"1": "easy", "2": "normal", "3": "hard"}
    difficulty = difficulty_mapping.get(difficulty)
    game = Game(difficulty)
    game.print_table()
    game.play()

if __name__ == "__main__":
    main()
