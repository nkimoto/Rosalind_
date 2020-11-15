#!/usr/bin/env python

"""
A solution to a ROSALIND bioinformatics problem.

Problem Title: Counting DNA Nucleotides: DNA
URL: http://rosalind.info/problems/dna/
"""

from utils.file_handler import load_seq
from Bio.Seq import Seq

def calc_ACGT_count(seq:Seq) -> str:
    """ Concatenate nucleotide counts in the order of  A, C, G, T splitted by space (' ')

    Arguments: Bio.Seq.Seq instance
    Returns: str 
    """
    ACGT_count_list = [seq.count("A"),
                       seq.count("C"),
                       seq.count("G"),
                       seq.count("T")]
    return " ".join([str(i) for i in ACGT_count_list])

print(calc_ACGT_count(load_seq("dna.txt")))

