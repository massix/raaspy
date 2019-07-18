from dataclasses import dataclass


@dataclass
class NumberObject(object):
    minimum: int
    maximum: int
    type: str
    result: int

    def serialize(self):
        return self.__dict__

