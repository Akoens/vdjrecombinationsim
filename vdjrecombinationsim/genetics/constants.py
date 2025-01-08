from enum import Enum

AMINO_ACIDS = {
    "A": "Alanine",
    "R": "Arginine",
    "N": "Asparagine",
    "D": "Aspartic acid",
    "C": "Cysteine",
    "E": "Glutamic acid",
    "Q": "Glutamine",
    "G": "Glycine",
    "H": "Histidine",
    "I": "Isoleucine",
    "L": "Leucine",
    "K": "Lysine",
    "M": "Methionine",
    "F": "Phenylalanine",
    "P": "Proline",
    "S": "Serine",
    "T": "Threonine",
    "W": "Tryptophan",
    "Y": "Tyrosine",
    "V": "Valine",
    "*": "Stop"  # Stop codon
}


class Heptamers(Enum):
    bp12 = ("CACTGTG", "GTGACAC")
    bp23 = ("CACAGTG", "GTGTCAC")


class Nonamers(Enum):
    bp12 = ("GGTTTTTGT", "CCAAAAACA")
    bp23 = ("ACAAAAACC", "TGTTTTTGG")


