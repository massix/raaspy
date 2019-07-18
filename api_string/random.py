from injector import inject
from model import StringObject
from random import randint
from typing import List


@inject
def get_random_string(size: int, allowed_characters: str):
    first_symbols = (33, 47)
    numbers = (48, 57)
    second_symbols = (58, 64)
    capitol_letters = (65, 90)
    third_symbols = (91, 96)
    letters = (97, 122)
    final_symbols = (123, 126)

    all = [first_symbols, numbers, second_symbols, capitol_letters, third_symbols, letters, final_symbols]

    if size <= 0 or size >= 126:
        size = 32

    allowed_characters_list: List[tuple] = []
    mapping = {k: v for k, v in locals().items() if v in all}
    allowed_characters_list = [v for k, v in mapping.items() if k in allowed_characters.split(',')]

    allowed_characters_list = all if len(allowed_characters_list) == 0 else allowed_characters_list

    random_string: str = ""
    for x in range(0, size):
        random_type = allowed_characters_list[randint(0, len(allowed_characters_list) - 1)]
        random_string += chr(randint(random_type[0], random_type[1]))

    return StringObject(random_string).serialize()
