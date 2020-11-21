#!/usr/bin/env python
"""
A solution to a ROSALIND bioinformatics problem.

Problem Title: Complementing a Strand of DNA
URL: http://rosalind.info/problems/revc/
"""

from utils.file_handler import load_seq
from Bio.Seq import Seq


def transcribe_DNA_to_RNA(seq: Seq) -> str:
    """ Transcribe DNA to RNA

    Arguments: Bio.Seq.Seq instance
    Returns: str 
    """
    return seq.reverse_complement()


print(transcribe_DNA_to_RNA(load_seq("rosalind_revc.txt")))
