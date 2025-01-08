from .sequence import Sequence

class Protein(Sequence):
    def __init__(self, sequence: str):
        super().__init__(sequence)