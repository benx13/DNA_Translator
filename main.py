#!/usr/bin/env python

"""main.py: translates a given dna sequence to its associate RNA and multipeptid sequence"""

__author__ = "BenX13"
__copyright__ = "Copyright 2019, For educational purposes"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "ahmed.sif.benmessaoud.13@gmail.com"



import re


class translate:
    def __init__(self, dna):
        self.dna = dna
        self.table = {
            'ATA': 'I',
            'ATC': 'I',
            'ATT': 'I',
            'ATG': 'M',
            'ACA': 'T',
            'ACC': 'T',
            'ACG': 'T',
            'ACT': 'T',
            'AAC': 'N',
            'AAT': 'N',
            'AAA': 'K',
            'AAG': 'K',
            'AGC': 'S',
            'AGT': 'S',
            'AGA': 'R',
            'AGG': 'R',
            'CTA': 'L',
            'CTC': 'L',
            'CTG': 'L',
            'CTT': 'L',
            'CCA': 'P',
            'CCC': 'P',
            'CCG': 'P',
            'CCT': 'P',
            'CAC': 'H',
            'CAT': 'H',
            'CAA': 'Q',
            'CAG': 'Q',
            'CGA': 'R',
            'CGC': 'R',
            'CGG': 'R',
            'CGT': 'R',
            'GTA': 'V',
            'GTC': 'V',
            'GTG': 'V',
            'GTT': 'V',
            'GCA': 'A',
            'GCC': 'A',
            'GCG': 'A',
            'GCT': 'A',
            'GAC': 'D',
            'GAT': 'D',
            'GAA': 'E',
            'GAG': 'E',
            'GGA': 'G',
            'GGC': 'G',
            'GGG': 'G',
            'GGT': 'G',
            'TCA': 'S',
            'TCC': 'S',
            'TCG': 'S',
            'TCT': 'S',
            'TTC': 'F',
            'TTT': 'F',
            'TTA': 'L',
            'TTG': 'L',
            'TAC': 'Y',
            'TAT': 'Y',
            'TAA': '_',
            'TAG': '_',
            'TGC': 'C',
            'TGT': 'C',
            'TGA': '_',
            'TGG': 'W',
            }

    def get_rna(self):
        rna = ''
        for i in self.dna:
            if i == 'A':
                rna += 'U'
            elif i == 'C':
                rna += 'G'
            elif i == 'G':
                rna += 'C'
            elif i == 'T':
                rna += 'A'
        return rna

    def get_protien(self):
        protein = []
        end = len(self.dna) - len(self.dna) % 3 - 1
        for i in range(0, end, 3):
            codon = self.dna[i:i + 3]
            if codon in self.table:
                aminoacid = self.table[codon]
                protein.append(aminoacid)
            else:
                protein.append('N')
        strprotein = ''.join(protein)
        finalprotien = re.findall('M[^M]*?_', strprotein)
        fl = []
        for i in finalprotien:
            fl.append(i[:-1])
        return fl

    def get_cgpercent(self):
        dna = self.dna.rstrip('\n')
        return (dna.count('G') + dna.count('C')) * 100 / len(dna)

