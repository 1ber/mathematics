#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Copyright (c) 2021 Humberto Ramos Costa
# ~ https://github.com/1ber
# ~ https://raw.githubusercontent.com/1ber/bio_informatics/main/License.txt
# ~ http://rosalind.info/problems/dna/

import os, sys

def main():
    
    # I lost my original file for the first problem, so i tested only
    # with the sambple dataset
    sample_dataset='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    
    counter={}
    for l in sample_dataset:
        ## The if assures that each letter is counted one time only
        if l not in counter.keys():
            counter[l]=sample_dataset.count(l)
    
    response=''
    # The solution values in the problem are ordered alphabetically, don't
    # know if it's on porpouse, but just ordered the keys here and the
    # values will be in the same order
    for k in sorted( counter.keys() ):
        #Already joining the values to the response string
        response=response+str( counter[k] )+' '
    
    # Print without the last space
    print( response[:-1] )
    
    sys.exit( 0 )

if __name__ == "__main__":

    main()
