#!/usr/bin/env python

"""
A solution to a ROSALIND bioinformatics problem.

Problem Title: Transcribing DNA into RNA
URL: http://rosalind.info/problems/rna/
"""

from utils.file_handler import load_seq
from Bio.Seq import Seq

def transcribe_DNA_to_RNA(seq:Seq) -> str:
    """ Transcribe DNA to RNA

    Arguments: Bio.Seq.Seq instance
    Returns: str 
    """
    return seq.transcribe()

print(transcribe_DNA_to_RNA(load_seq("rosalind_rna.txt")))