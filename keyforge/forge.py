from secrets import choice
from secrets import randbelow

def rand_between(min_val, max_val):
    return randbelow(max_val - min_val + 1) + min_val

def random_letter():
    upper_or_lower = randbelow(2)
    if upper_or_lower == 0:
        return rand_between(65, 90)
    else:
        return rand_between(97, 122)

def random_digit():
    return rand_between(48, 57)

def random_special():
    special_block = randbelow(4)
    if special_block == 0:
        return rand_between(33, 47)
    elif special_block == 1:
        return rand_between(58, 64)
    elif special_block == 2:
        return rand_between(91, 96)
    elif special_block == 3:
        return rand_between(123, 126)

def forge_password(length, alpha, numeric, special, combo):
    char_classes = set()
    if combo:
        char_classes.add('a')
        char_classes.add('n')
        char_classes.add('s')
    elif alpha:
        char_classes.add('a')
    elif numeric:
        char_classes.add('n')
    elif special:
        char_classes.add('s')

    password = ""
    if char_classes:
        while True:
            char_class = choice(list(char_classes))
            if 'a' in char_class:
                password += chr(random_letter())
            elif 'n' in char_class:
                password += chr(random_digit())
            elif 's' in char_class:
                password += chr(random_special())

            if length is not None:
                if len(password) == length:
                    break

