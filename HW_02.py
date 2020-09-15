# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 10:37:40 2020

@author: tranc
"""

finish = 'c' # initialize finish to a value different than n
while finish != 'n':
    seq1= str.upper(input('Enter sequence 1 using only A,G,T,C, or U: \n'))
    seq2= str.upper(input('Enter sequence 2 using only A,G,T,C, or U: \n'))
    Total1 = 0
    Total2 = 0
    seqID = 0.0
    same = 0
    Error = False
    for i in seq1:
        if i not in 'ATGCU':
            print('\nERROR, sequence 1 must contain only G,C,A,T or U. ')
            Error = True
            break
        Total1 = Total1 + 1
    seq1 =seq1.replace('T','U')
    
    for n in seq2:
        if n not in 'ATGCU':
            print('\nERROR, sequence 2 must contain only G,C,A,T or U. ')
            Error = True
            break
        Total2 = Total2 + 1
    seq2 = seq2.replace('T','U')
   
    if not Error:
        if Total1 != Total2:
            print('\nERROR, the sequences must be the same length. \n')
            Error = True
        else:
            for i,n in zip(seq1, seq2):
                if i == n:
                    same = same + 1
            seqID = same/Total1
            print('\nThe sequence ID between the two sequences of length', Total1, 'is', seqID)
    else:
        continue
    finish = input('Would you like to enter a new sequence? Enter any key to continue or "n" to stop. \n')
    
print('Thank you and have a good day!')
       