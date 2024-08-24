# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:11:22 2024

@author: kieu0
"""

gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút "))
giay = int(input("NHập giây "))
tong_giay = gio * 3600 + phut * 60 + giay
print("Tổng giây là: ", tong_giay)