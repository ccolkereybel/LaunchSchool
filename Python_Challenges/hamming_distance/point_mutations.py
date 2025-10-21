"""
The Hamming distance is only defined for sequences of equal length.
If you have two sequences of unequal length,
you should compute the Hamming distance over the shorter length.

Compare two strings
-count the number of differences

If string of different lengths
-compare hamming distance over shorter lengths

DNA strand passed in to create class instance
hamming_distance is set by calling a class method
    -DNA strand passed into this method
    -outputs the number of differences from this string to DNA string
"""

class DNA:
    def __init__(self, strand1):
        self.strand1 = strand1
        
    def hamming_distance(self, strand2):
        count = 0
        for letter1, letter2 in zip(self.strand1, strand2):
            if letter1 != letter2:
                count += 1

        return count
