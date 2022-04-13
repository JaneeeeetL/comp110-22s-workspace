"""Utility class for numerical operations."""

from __future__ import annotations
from optparse import Values
from types import UnionType

from typing import Union

__author__ = "730401522"


class Simpy:
    """An object of EX09."""
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, values: list[float]):
        """Construct a Simpy object."""
        self.values = values

    def __str__(self) -> str:
        """A str representation of the Simpy object."""
        return f"Simpy({self.values})"

    def fill(self, nums_f: float, times: int) -> None:
        """This method fills an empty Simpy object."""
        while len(self.values) != 0:
            self.values.clear()
        while len(self.values) < times:
            self.values.append(nums_f)
        
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """This method fills the empty Simpy object with values within a specific range with certain steps."""
        assert step != 0.0
        i: int = 0
        n: float = (stop - start) / step
        while len(self.values) != 0:
            self.values.clear()
        while i < n:
            self.values.append(start + step * i)
            i += 1

    def sum(self) -> float:
        """This method computes and return the sum of all items in values."""
        return sum(self.values)

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Adds two sides together."""
        if isinstance(rhs, Simpy):
            result: list[float] = []
            for i in range(0, len(self.values)):
                result.append(self.values[i] + rhs.values[i])
            return Simpy(result)
        else:
            result: list[float] = []
            for item in self.values:
                result.append(item + rhs)
            return Simpy(result)

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Raises one side to the power of other side."""
        if isinstance(rhs, Simpy):
            result: list[float] = []
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
            return Simpy(result)
        else:
            result: list[float] = []
            for item in self.values:
                result.append(item ** rhs)
            return Simpy(result)
    
    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Checks equality of two sides."""
        if isinstance(rhs, Simpy):
            result: list[bool] = []
            for i in range(0, len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
            return result
        else:
            result: list[bool] = []
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
            return result
    
    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Checks 'greater than' of two sides."""
        if isinstance(rhs, Simpy):
            result: list[bool] = []
            for i in range(0, len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
            return result
        else:
            result: list[bool] = []
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
            return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """A method that helps with filtering values."""
        if isinstance(rhs, int):
            i: int = 0
            while i < len(self.values):
                if self.values[i] == self.values[rhs]:
                    return self.values[rhs]
                i += 1
        else:
            result: list[float] = []
            i: int = 0
            while i < len(rhs):
                if rhs[i]:
                    result.append(self.values[i])
                i += 1
            return Simpy(result)
        

    # def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
    #     """overloading method of __getitem__."""
    #     result: list[float] = []
    #     if isinstance(rhs, int):
    #         mask_i: int = rhs
    #         for item in self.values:
    #             if item > mask_i:
    #                 result.append(item)
    #     else:
    #         mask_b = rhs
    #         i: int = 0
    #         while i < len(mask_b):
    #             if mask_b[i]:
    #                 result.append(self.values[i])
    #             i += 1
    #         # for item in self.values:
    #         #     index: int = item
    #         #     if mask_b[index] == True:
    #         #         result.append(self[item])
    #         return result
    #     return Simpy(result)

            
            
            
