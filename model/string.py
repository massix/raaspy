from dataclasses import dataclass


@dataclass
class StringObject(object):
    result: str

    def serialize(self):
        return self.__dict__.copy()

    @classmethod
    def deserialize(cls, **dictionary) -> 'StringObject':
        s = object.__new__(StringObject)
        s.__dict__ = dictionary.copy()
        return s
