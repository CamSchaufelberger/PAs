# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:40:25 2024

@author: CDSchaufelberger
"""
#PART ONE
import numpy as np

#problem one
p = np.poly1d([2,3,0,1])
print(np.poly1d(p))
print(p(2))


#derivative of polynomial(problem 2)
p = np.poly1d([1,0,1])
p2 = np.polyder(p)
print(p2(1))

#%%

#PART TWO

question = input("What is your polynomial? ")
poly = [float(pol) for pol in question.split(',')]
x_1 = float(input("What is your x_1 value? "))

def eval_poly(poly, x):
    return np.polyval(poly,x)
    
def eval_der(poly,x):
    d = np.polyder(poly)
    p2 = np.polyval(d,x)
    return p2

def newtons_method(poly, x_new, iteration = 1):
    x_x = eval_poly(poly, x_new)
    x_x_p = eval_der(poly, x_new)
    x_n_p = x_new - x_x/x_x_p
    print(f"x_{iteration} = {x_new}")
    if abs(x_n_p - x_new) < .001:
        return x_n_p
    else: 
        return newtons_method(poly, x_n_p, iteration + 1)

print(f"The final value with stabilized thousandths place is: {newtons_method(poly, x_1)}")
print(f"The roots of this function are: {np.roots(poly)}")


