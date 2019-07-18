from dataclasses import dataclass


@dataclass
class StringObject(object):
    result: str

    def serialize(self):
        return self.__dict__
