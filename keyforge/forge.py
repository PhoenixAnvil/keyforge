from secrets import choice
from secrets import randbelow


def rand_between(min_val, max_val):
    return randbelow(max_val - min_val + 1) + min_val


def random_letter():
    upper_or_lower = randbelow(2)
    if upper_or_lower == 0:
        return chr(rand_between(65, 90))
    else:
        return chr(rand_between(97, 122))


def random_digit():
    return chr(rand_between(48, 57))


def random_special():
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
    while length is None or len(password) < length:
        char_class = choice(list(char_classes))
        if char_class == "a":
            password += random_letter()
        elif char_class == "n":
            password += random_digit()
        elif char_class == "s":
            password += random_special()

    return password
