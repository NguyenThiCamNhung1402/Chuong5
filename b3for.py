# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 18:42:26 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
import random
so_luong = random.randint(20, 30)
danh_sach = [random.randint(18, 99) ** 2 for i in range(so_luong)]
print(f"Số lượng phần tử: {so_luong}")
print("Danh sách bình phương của các số thực ngẫu nhiên:")
print(danh_sach)

