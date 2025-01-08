from __future__ import annotations
from abc import ABC, abstractmethod

class Sequence(ABC):
    @abstractmethod
    def __init__(self, sequence: str):
        """
        The Sequence object is for
        Check sequence variable for required type and length then storing it.
        :param sequence:
        """

        if type(sequence) is not str:
            raise TypeError("Sequence must be a string")

        if len(sequence) == 0:
            raise ValueError("Empty sequence")

        # Keep sequence as a private variable
        self._sequence = sequence

    @property
    def sequence(self):
        """
        Sequence is defined as a property to make it static and ensure it can not be altered externally.
        :return: The content of the sequence as a string.
        """
        return self._sequence

    @sequence.getter
    def get_sequence(self) -> str:
        """
        The getter is so the sequence string can still be retrieved from the sequence object.
        :return: Sequence as a string.
        """
        return self.sequence

    def __len__(self) -> int:
        """
        Returns the length of the DNA sequence.
        :return: length of sequence as int.
        """
        return len(self.sequence)

    def __eq__(self, other: Sequence) -> bool:
        """
        Compares the _sequence of this instance against the other. So the two can be differentiated
        :param other: Another instance of DNA sequence.
        :return: Boolean of equality between the two instances.
        """
        # Check if other is instance of DNA
        if not isinstance(other, Sequence):
            return False
        # Return equality of sequences
        return self.sequence == other.sequence

    def __str__(self) -> str:
        """
        Returns this DNA sequence string in case of object being accessed
        in a context where it needs to be readable.
        :return: string representation of this DNA sequence.
        """
        return self.sequence