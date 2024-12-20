from __future__ import annotations
from .sequence import Sequence


class DNA(Sequence):
    """
    The DNA class is a subclass of the Sequence class that implements methods that help in handling and altering of DNA
    sequences.
    """
    NUCLEOTIDES = {'A', 'T', 'C', 'G'}
    COMPLEMENT_NUCLEOTIDES = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    CODON_TO_AMINO_ACIDS = {
        'TTT': 'F', 'TTC': 'F',  # Phenylalanine
        'TTA': 'L', 'TTG': 'L',  # Leucine
        'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',  # Leucine
        'ATT': 'I', 'ATC': 'I', 'ATA': 'I',  # Isoleucine
        'ATG': 'M',  # Methionine (Start codon)
        'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',  # Valine
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',  # Serine
        'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',  # Proline
        'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',  # Threonine
        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',  # Alanine
        'TAT': 'Y', 'TAC': 'Y',  # Tyrosine
        'TAA': '*', 'TAG': '*', 'TGA': '*',  # Stop codons
        'CAT': 'H', 'CAC': 'H',  # Histidine
        'CAA': 'Q', 'CAG': 'Q',  # Glutamine
        'AAT': 'N', 'AAC': 'N',  # Asparagine
        'AAA': 'K', 'AAG': 'K',  # Lysine
        'GAT': 'D', 'GAC': 'D',  # Aspartic acid
        'GAA': 'E', 'GAG': 'E',  # Glutamic acid
        'TGT': 'C', 'TGC': 'C',  # Cysteine
        'TGG': 'W',  # Tryptophan
        'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',  # Arginine
        'AGT': 'S', 'AGC': 'S',  # Serine
        'AGA': 'R', 'AGG': 'R',  # Arginine
        'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'  # Glycine
    }

    def __init__(self, sequence: str) -> None:
        """
        This class is initialized with a sequence of valid DNA nucleotides in the form of capital ATCG characters.
        :param sequence: a string containing DNA nucleotides.
        """

        # Check if nucleotides in sequence are valid.
        if not set(sequence) <= set(self.NUCLEOTIDES):
            raise ValueError('Sequence must contain valid nucleotides')

        # Instantiate super with sequence.
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

    def translate(self, sliding_window = 0):
        """
        Translates the DNA sequence to a protein sequence.
        :return: A protein sequence as an instance of Sequence.
        """
        # Split sequence into codons.
        codons = [self.sequence[i:i + 3] for i in range(sliding_window, len(self.sequence), 3)]

        # Translate the codons to acids and join them on a string.
        acids = ''.join([self.CODON_TO_AMINO_ACIDS[codon] for codon in codons])

        # Return an instance of Sequence containing the protein sequence.
        return Sequence(acids)
