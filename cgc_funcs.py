"""
cgc_funcs.py - small library of functions for analysis of the CapGapCap resonator design

Evan, 2018

"""

__version__ = '0.1'
__author__ = 'Evan'



from pandas import read_csv




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Capacitor analytical functions

def calculate_C(eps, A, d):
    return eps*A/d

def p_ox(A, t, d , eps_r):
    # calculate oxide filling factor for thickness t on EACH plate
    return 2*t / (2*t + eps_r*(d-2*t))







# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# I/O functions for reading in simulation results
