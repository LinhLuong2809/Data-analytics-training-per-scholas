'''
This is the module to calculate interest for promblem 3 in python SBA 
'''

def calculate_simple_interest(principal, rate, time): # function to calculate simple interest
    simple_interest = (principal * rate * time) / 100 # Formula: Simple Interest (SI) = (Principal * Rate * Time) / 100
    return simple_interest # return the value to function

def calculate_compound_interest(principal, rate, time): # function to calculate compound interest
    compound_interest = (principal * ((1 + rate / 100) ** time)) - principal # Formula: Compound Interest (CI) = Principal * (1 + Rate/100)^Time - Principal
    return compound_interest # return value to function