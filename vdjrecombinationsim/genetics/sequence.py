from __future__ import annotations

class Sequence(object):
    def __init__(self, sequence: str):
        if type(sequence) is not str:
            raise TypeError('Sequence must be a string')

        if len(sequence) == 0:
            raise ValueError("Empty sequence")

        self._sequence = sequence

    @property
    def sequence(self):
        return self._sequence

    @sequence.getter
    def get_sequence(self) -> str:
        return self.sequence

    def __len__(self) -> int:
        """
        Returns the length of the DNA sequence.
        :return: length of sequence as int
        """
        return len(self.sequence)

    def __eq__(self, other: Sequence) -> bool:
        """
        Compares the _sequence of this instance against the other.
        :param other: Another instance of DNA sequence.
        :return: boolean of equality between the two instances.
        """
        # Check if other is instance of DNA
        if not isinstance(other, Sequence):
            return False
        # Return equality of sequences
        return self.sequence == other.sequence