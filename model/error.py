from dataclasses import dataclass


@dataclass
class Error(object):
    code: int
    description: str

    def serialize(self):
        return self.__dict__
