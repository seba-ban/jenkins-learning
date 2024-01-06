from typing import Generic, TypeVar

T = TypeVar('T')
P = TypeVar('P')


class Adder(Generic[T, P]):
    def add(self, x: T, y: T) -> P:
        """Add implementation."""