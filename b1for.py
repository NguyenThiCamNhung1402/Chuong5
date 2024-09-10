# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 18:25:05 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
n = int(input("Nhập số nguyên dương n: "))
giai_thua = 1
if n>0:
    for i in range(1, n + 1):
        giai_thua *= i
else:
    n=int(input("Số nhập vào phải là số nguyên dương.Mời nhập lại:"))
    for i in range(1, n + 1):
        giai_thua *= i
print(f"Giai thừa của {n} là {giai_thua}")
