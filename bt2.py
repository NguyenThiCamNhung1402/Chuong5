# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:33:58 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
ds = [num for num in range(2020, 3838) if num % 2 == 0]
new_ds= [i for i in ds if i %9==0 ]
chuoi = ''
for x in new_ds:
    if chuoi: 
        chuoi += '\t' 
    chuoi += str(x)  
print(chuoi)