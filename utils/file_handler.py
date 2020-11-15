#!/usr/bin/env python

import os
from Bio.Seq import Seq

def load_seq(file_name: str, dir_name: str ="data") -> Seq:
    """
    Arguments:
        file_name: Input file name
        dir_name: Input directory name

    Returns:
        Bio.Seq.Seq instance
    """
    file_path = os.path.join(dir_name, file_name)
    with open(file_path, "r") as rf:
        seq_str = rf.read().strip()
    seq = Seq(seq_str)
    return seq