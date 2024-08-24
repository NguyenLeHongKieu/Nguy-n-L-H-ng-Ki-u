# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:01:35 2024

@author: kieu0
"""

N = int(input("Nhập số nguyên có hai chữ số: "))
if 10<=N<=99:
    hang_chuc = N // 10
    hang_don_vi = N % 10
    tong_chu_so = hang_chuc + hang_don_vi
    print("Tổng các chữ số của N là: ", tong_chu_so)
else:
    print("Số nhập vào không phải số nguyên dương có hai chữ số.")