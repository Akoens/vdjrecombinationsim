from __future__ import annotations

from .sequence import Sequence


class DNA(Sequence):
    _nucleotides = {'A', 'T', 'C', 'G'}
    _compliment_nucleotides = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    _codon_to_amino_acid = {
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

        if not set(sequence) <= set(self._nucleotides):
            raise ValueError('Sequence must contain valid nucleotides')

        super().__init__(sequence)

    def _complement(self) -> str:
        complement_sequence = ''.join(self._compliment_nucleotides[nucleotide] for nucleotide in self.sequence)
        return complement_sequence

    def compliment(self) -> DNA:
        complement = self._complement()
        return DNA(complement)

    def reverse_complement(self) -> DNA:
        reverse_complement_sequence = self._complement()[::-1]
        return DNA(reverse_complement_sequence)

    def translate(self):
        codons = [self.sequence[i:i + 3] for i in range(0, len(self.sequence), 3)]
        acids = ''.join([self._codon_to_amino_acid[codon] for codon in codons])
        return Sequence(acids)

    def __eq__(self, other):
        return self.sequence == other.sequence
