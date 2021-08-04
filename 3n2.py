#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Copyright (c) 2021 Humberto Ramos Costa
from math import inf
from matplotlib import pyplot as plt
from scipy.ndimage.filters import gaussian_filter1d
import mplcyberpunk, os, sys, random



def main():
    # ~ plt.style.use("cyberpunk")
    
    # ~ plt.ion()
    # ~ x=[]
    # ~ y=[]
    for m in range( 1, 100, 2 ):
        m_b=bin(m)[2:]
        n=m
        ns_b=[]
        while( bin(n)[2:].count('1') != 1 ):
            print( n )
            n=(3*m)+1
            ns_b.append( n )
            # ~ n_b=bin(n)[2:]
        print( m, m_b, ns_b )

        # ~ m=
        # ~ n_d=n_b.count('1' )/len(n_b)
        # ~ x.append( n_d )
        # ~ y.append( len( generate( n ) ) )

    sys.exit( 0 )


if __name__ == "__main__":
    

    main()

