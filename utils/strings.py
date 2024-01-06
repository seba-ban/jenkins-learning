from typing import Union
from .interface import Adder

StrOrInt = Union[str, int]

class StringAdder(Adder[StrOrInt, int]):
    def _assure_int(self, x: StrOrInt) -> int:
        if isinstance(x, int):
            return x
        return int(x)
    
    def add(self, x, y):
        return self._assure_int(x) + self._assure_int(y)