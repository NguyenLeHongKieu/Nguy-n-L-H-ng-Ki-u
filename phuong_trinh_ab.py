# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:07:04 2024

@author: kieu0
"""

a = int(input("Nhập số thực a: "))
b = int(input("Nhập số thực b: "))
A = (a**(1/2) - (b**(1/2))) / ((a**(1/4) - b**(1/4))) - ((a**(1/2) + (a*b)**(1/4)) / (a**(1/4) + b**(1/4)))
print("Kết quả: ", A)