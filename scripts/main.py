"""
This Project simulates the recombination of the vdj segments in developing
lymphocytes during the early stages of T and B cell maturation.

Create on 2024-12-16 11:23
A F Koens
"""

# Define & Create Germline DNA
# Definition of Heptamer and Nonamer
# Define Recombination Signal Sequences(RSSs)
# light and Heavy chains alternatives (VJ & VDJ)
# RAG "identifying RSS"
# Cleaving of sequence

from Bio.Seq import Seq



def main():
    # create a sequence object
    my_seq = Seq("CATGTAGACTAG")

    # print out some details about it
    print("seq %s is %i bases long" % (my_seq, len(my_seq)))
    print("reverse complement is %s" % my_seq.reverse_complement())
    print("protein translation is %s" % my_seq.translate())

if __name__ == '__main__':
    main()
