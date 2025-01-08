"""
This Project simulates the recombination of the vdj segments in developing
lymphocytes during the early stages of T and B cell maturation.

Create on 2024-12-16 11:23
A F Koens
"""

# - [X] Define & Create Germline DNA
# - [X] Definition of Heptamer and Nonamer
# - [ ] Search for Recombination Signal Sequences(RSSs) with the "RAG(enzyme)" function that identifies RSSs"
# - [ ] Cleaving of sequence (removing excess DNA)
# - [ ] Introduce Random nucleotides at cutoff point.
# - [ ] Check for valid proteins e.g. they can be translated from start to stop

from genetics.dna import DNA

def main():
    # create a sequence object
    my_seq = DNA("CATGTAGACTAG")

    # print out some details about it
    print("seq %s is %i bases long" % (my_seq, len(my_seq)))
    print("reverse complement is %s" % my_seq.reverse_complement())
    print("protein translation is %s" % my_seq.translate(start_from="ATG"))

if __name__ == '__main__':
    main()
