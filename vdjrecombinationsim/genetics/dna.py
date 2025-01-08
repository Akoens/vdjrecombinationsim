from __future__ import annotations

from multiprocessing.managers import Value

from .sequence import Sequence
from .protein import Protein


class DNA(Sequence):
    # TODO refactor all the constants into the constants file.
    NUCLEOTIDES = {"A", "T", "C", "G"}
    COMPLEMENT_NUCLEOTIDES = {"A": "T", "T": "A", "C": "G", "G": "C"}
    CODON_TO_AMINO_ACIDS = {
        "TTT": "F", "TTC": "F",  # Phenylalanine
        "TTA": "L", "TTG": "L",  # Leucine
        "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",  # Leucine
        "ATT": "I", "ATC": "I", "ATA": "I",  # Isoleucine
        "ATG": "M",  # Methionine (Start codon)
        "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",  # Valine
        "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",  # Serine
        "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",  # Proline
        "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",  # Threonine
        "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",  # Alanine
        "TAT": "Y", "TAC": "Y",  # Tyrosine
        "TAA": "*", "TAG": "*", "TGA": "*",  # Stop codons
        "CAT": "H", "CAC": "H",  # Histidine
        "CAA": "Q", "CAG": "Q",  # Glutamine
        "AAT": "N", "AAC": "N",  # Asparagine
        "AAA": "K", "AAG": "K",  # Lysine
        "GAT": "D", "GAC": "D",  # Aspartic acid
        "GAA": "E", "GAG": "E",  # Glutamic acid
        "TGT": "C", "TGC": "C",  # Cysteine
        "TGG": "W",  # Tryptophan
        "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",  # Arginine
        "AGT": "S", "AGC": "S",  # Serine
        "AGA": "R", "AGG": "R",  # Arginine
        "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"  # Glycine
    }

    def __init__(self, sequence: str) -> None:
        """
        This class is initialized with a sequence of valid DNA nucleotides in the form of capital ATCG characters.
        :param sequence: a string containing DNA nucleotides.
        """

        if not set(sequence) <= set(self.NUCLEOTIDES):
            raise ValueError('Sequence must contain valid nucleotides.')

        super().__init__(sequence)

    def _complement(self) -> str:
        """
        This functions generates a complement string to the DNA sequence str.
        :return: a complement DNA sequence as a string.
        """
        complement_sequence = ''.join(self.COMPLEMENT_NUCLEOTIDES[nucleotide] for nucleotide in self.sequence)
        return complement_sequence

    def compliment(self) -> DNA:
        """
        Creates a complemented DNA sequence.
        :return: DNA instance containing a complemented DNA sequence.
        """
        complement = self._complement()
        return DNA(complement)

    def reverse_complement(self) -> DNA:
        """
        Creates a reverse complemented DNA sequence.
        :return: DNA instance containing a reverse complemented DNA sequence.
        """
        reverse_complement_sequence = self._complement()[::-1]
        return DNA(reverse_complement_sequence)

    def translate(self, start_from: int | str = 0) -> Protein:
        """
        Translates the DNA sequence to a protein sequence.
        :param start_from: start index of the DNA sequence or start from index of subsequence matching string.
        :return: A protein sequence as an instance of Sequence.
        """


        if type(start_from) is not int and type(start_from) is not str :
            raise TypeError(f"Keyword argument 'start_from' can only be int or str, {type(start_from)} was given.")


        # If a subsequence str is given as an argument find the first match in the sequence
        if type(start_from) is int:
            sliding_window = start_from
        else:
            sliding_window = self.sequence.find(start_from)

        # TODO check for codons shorter than 3, either trim them?
        # TODO implement check on stop codon, have it cut off
        # Split sequence into codons with reading frame starting at 0.
        codons = [self.sequence[i:i + 3] for i in range(sliding_window, len(self.sequence), 3)]

        # Translate the codons to acids and combine them to form a protein.
        acids = "".join([self.CODON_TO_AMINO_ACIDS[codon] for codon in codons])
        protein = Protein(acids)

        return protein


