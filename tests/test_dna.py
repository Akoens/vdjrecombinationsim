import pytest
from vdjrecombinationsim.genetics.dna import DNA


@pytest.mark.parametrize('sequence', [None, int(), float(), tuple(), list(), set(), dict()])
def test_incorrect_datatype(sequence):
    with pytest.raises(TypeError):
        # noinspection PyTypeChecker
        DNA(sequence)


def test_empty_sequence():
    with pytest.raises(ValueError):
        DNA('')


def test_incorrect_nucleotides_in_sequence():
    with pytest.raises(ValueError):
        DNA('AGTC~?/')


@pytest.mark.parametrize('sequence,expected', [
    ('TATGCGGTAA', 'ATACGCCATT'),
    ('TTACTTTCTC', 'AATGAAAGAG'),
    ('GTTGGATATC', 'CAACCTATAG'),
    ('GGCGTTGTAG', 'CCGCAACATC'),
    ('CTCAGTTGAC', 'GAGTCAACTG')
])
def test_complement_sequence(sequence, expected):
    assert DNA(sequence).compliment() == DNA(expected)


@pytest.mark.parametrize('sequence,expected', [
    ('ATGTATGCAG', 'CTGCATACAT'),
    ('TGGGGCACTA', 'TAGTGCCCCA'),
    ('TGTTGTTCCT', 'AGGAACAACA'),
    ('TCGCATCTGG', 'CCAGATGCGA'),
    ('AGGGTCAGTG', 'CACTGACCCT')
])
def test_reverse_complement(sequence, expected):
    assert DNA(sequence).reverse_complement() == DNA(expected)
