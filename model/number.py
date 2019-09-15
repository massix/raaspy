from dataclasses import dataclass


@dataclass
class NumberObject(object):
    minimum: int
    maximum: int
    type: str
    result: int

    def serialize(self):
        return self.__dict__.copy()

    @classmethod
    def deserialize(cls, **dictionary) -> 'NumberObject':
        n = object.__new__(NumberObject)
        n.__dict__ = dictionary.copy()
        return n
