"""
-- *********************************************
-- Author       :	Sharlotte Manganye
-- Create date  :   05 January 2021
-- Description  :   Cost Functions
-- File Name    :   fitness_functions.py these function where selected based on popularity in the PSO community
--
"""
import numpy as np


def sphere(X):
    total = 0
    for i in range(len(X)):
        total  += X[i] ** 2
    return total


def rosenbrock(X):
    sigma = 0
    for i in range(int(len(X)/2)):
        a = X[(2 * i) - 1]
        sigma += 100 * np.power((X[2*i] - np.power(a, 2)), 2) + np.power((1 - a), 2)
    return sigma


def ackley(X, a=20, b=0.2, c=2*np.pi):
    ackley = 0
    d = len(X)
    for i in range(d):
        sum_sq_term = -a * np.exp(-b * np.sqrt((X[i] * X[i]) / d))
        cos_term = -np.exp((np.cos(c * X[i]) / d))
        ackley += a + np.exp(1) + sum_sq_term + cos_term
    return ackley


def rastrigin(X):
    rastrigin = 0
    n = len(X)
    for i in range(n):
        rastrigin += (X[i] ** 2 - 10 * np.cos(2 * np.pi * X[i]) + 10)
    return rastrigin

def griewank(X):
    sigma = 0
    for i in range(len(X)):
        sigma += X[i] ** 2
        product_part = 1
    for i in range(len(X)):
        product_part *= np.cos((X[i]) / np.sqrt(i + 1))
    return 1 + ((sigma) / 4000) - (product_part)