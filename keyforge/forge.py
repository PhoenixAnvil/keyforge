"""
forge.py - Core password generation logic for the KeyForge CLI tool.

This module provides cryptographically secure functions to generate random
characters (letters, digits, and special symbols), along with a flexible
password generation engine that supports different character class options.
"""

from secrets import choice
from secrets import randbelow


def rand_between(min_val, max_val):
    """
    Return a cryptographically secure random integer between min_val and max_val (inclusive).
    """
    return randbelow(max_val - min_val + 1) + min_val


def random_letter():
    """
    Generate a random alphabetic character (uppercase or lowercase).
    """
    upper_or_lower = randbelow(2)
    if upper_or_lower == 0:
        return chr(rand_between(65, 90))
    else:
        return chr(rand_between(97, 122))


def random_digit():
    """
    Generate a random digit character (0-9).
    """
    return chr(rand_between(48, 57))


def random_special():
    """
    Generate a random special character from one of four ASCII symbol ranges.
    """
    special_block = randbelow(4)
    if special_block == 0:
        return chr(rand_between(33, 47))
    elif special_block == 1:
        return chr(rand_between(58, 64))
    elif special_block == 2:
        return chr(rand_between(91, 96))
    elif special_block == 3:
        return chr(rand_between(123, 126))


def forge_password(length, alpha, numeric, special, combo):
    """
    Generate a secure password using the specified character classes.

    Parameters:
        length (int): Desired length of the password.
        alpha (bool): Use alphabetic characters only.
        numeric (bool): Use numeric characters only.
        special (bool): Use special characters only.
        combo (bool): Use a combination of all three character types.

    Returns:
        str: The generated secure password.
    """
    char_classes = set()
    if combo:
        char_classes.update({"a", "n", "s"})
    elif alpha:
        char_classes.add("a")
    elif numeric:
        char_classes.add("n")
    elif special:
        char_classes.add("s")

    password = ""
    while len(password) < length:
        char_class = choice(list(char_classes))
        if char_class == "a":
            password += random_letter()
        elif char_class == "n":
            password += random_digit()
        elif char_class == "s":
            password += random_special()

    return password
