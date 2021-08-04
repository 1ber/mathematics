#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Copyright (c) 2021 Humberto Ramos Costa
from math import inf
from matplotlib import pyplot as plt
from scipy.ndimage.filters import gaussian_filter1d
import mplcyberpunk, os, sys, random


def tob( n ):
    return ( bin(n)[2:] )


def generate_a( n ):
    l=[]
    p=0
    i=0
    while( True ):
        l.append( [n, tob(n)] )
        if( n == 1 ):
            break
        if( n % 2 == 0 ):
            p=p+1
            n=int( n/2 )
        else:
            i=i+1
            n=( 3*n + 1 )

    return ( l )

    
def generate_b( n ):
    n1=n
    l1=[]
    p=0
    i=1
    while( True ):
        l1.append( n1 )
        if( n1 == 1 ):
            break
        
        if( n1 % 2 == 0 ):
            p=p+1
            n1=int( n1/2 )
        else:
            i=i+1
            n1=( 3*n1 + 1 )
    
    l2=[]
    for i in range( i ):
        l2.append( n )
        n=( 3*n + 1 )
        
    for i in range( p ):
        l2.append( n )
        n=int( n/2 )
            
    return ( i, l1, l2 )


def generate_c( n ):
    x=( 3*n )
    return( n, tob(n), x, tob(x) )
    
def generate_d( a ):
    x=( (6*a)+4 )
    return( a, a*2+1, x, tob(x) )


def generate_d( n ):
    r=(3*n) +2
    
    return ( [tob(n), r,tob(r) ] )
    
def tn1( n ):
    return( 3*n + 1 )
    
def count1( n ):
    return( tob(n).count('1' ) )
    
def countbpot( n ):
    r=[]
    c=0
    i=0
    while( True ):
        if( count1( i ) == 1 ):
            r.append([i, c ])
            c=0
        else:
            c=c+1
        i=i+1
        if( i == n ):
            break
    return( r )
        

def count_div_2( n ):
    c=0
    while ( n>1 and n % 2 == 0 ):
        c=c+1
        n=int( n/2 )
        # ~ print( n )
    return( c )
        


def main():
    for i in range( 100 ):
        n=count_div_2( i )
        if( n == 0 ):
            n=count_div_2( tn1( i ) )
        print( i, n )
    # ~ x=range( 1, 1000, 2 )
        
    # ~ plt.style.use("cyberpunk")
    # ~ plt.plot( x,  [ count1( tn1(n) ) for n in x ]  )
    # ~ plt.show()

    sys.exit( 0 )


if __name__ == "__main__":
    

    main()

