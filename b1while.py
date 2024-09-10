# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 18:59:40 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
n= float(input("Nhập một giá trị trong khoảng từ -99 đến 99: "))
while n<= -99 or n>=99:
    n= float(input("Nhập lại giá trị: "))
print(f"Giá trị đã nhập {n} thỏa mãn điều kiện")