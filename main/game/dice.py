import random
import math

class Dice:
    def __init__(self):
        pass

    def roll_die(self, num_dice, sides):
        """
        Rolls a single type of die.

        Args:
            num_dice: The number of dice to roll.
            sides: The number of sides on each die.

        Returns:
            A list containing:
                - A list of the individual die rolls.
                - The sum of all the rolls.
        """
        rolls = []
        for _ in range(num_dice):
            rolls.append(random.randint(1, sides))
        return rolls, sum(rolls)

    def roll_dice(self, dice_strings):
        """
        Rolls multiple sets of dice.

        Args:
            dice_strings: A list of strings, where each string 
                         represents a set of dice in the format "NdS" 
                         (e.g., "2d6", "1d20").

        Returns:
            A list of results, where each result is a list containing:
                - A list of the individual die rolls for that set.
                - The sum of all the rolls for that set.
        """
        if not dice_strings:
            return "No dice"

        results = []
        for dice_str in dice_strings:
            num_dice, sides = map(int, dice_str.split("d"))
            results.append(self.roll_die(num_dice, sides))
        return results

    def roll(self):
        """
        Prompts the user for dice input and rolls the specified dice.

        Returns:
            The results of the dice rolls, or "cancelled" if the user 
            presses Enter without input.
        """
        user_input = input("Enter desired dice and press enter or press enter to cancel \nExamples: '1d6'/'1d6,1d20'/'6d6'/ 1d6,20d20'/'1d6A'/'1d6D' ")
        if user_input == "":
            return "cancelled"
        else:
            dice_list = user_input.split(",")
            return self.roll_dice(dice_list)

