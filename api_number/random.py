import random
from injector import inject
from model import NumberObject, Error


@inject
def get(p_min: int, p_max: int):
    p_max = 100 if p_max == 0 else p_max
    return NumberObject(minimum=p_min, maximum=p_max, type="integer", result=random.randint(p_min, p_max)).serialize() \
        if p_max >= p_min else (Error(code=400, description="Maximum should be higher than Minimum").serialize(), 400)


@inject
def get_scrum(p_max: int):
    p_max = 100 if p_max == 0 else p_max
    original_sequence = [0.5, 1, 2, 3, 5, 8, 12, 20, 40, 100]
    allowed_sequence = [f for f in original_sequence if f <= p_max]
    return NumberObject(minimum=0,
                        maximum=p_max,
                        result=allowed_sequence[random.randint(0, len(allowed_sequence) - 1)],
                        type="fibonacci")\
        .serialize()
