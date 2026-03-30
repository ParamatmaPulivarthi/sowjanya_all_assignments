# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 16:44:20 2026

@author: hp
"""

import pandas as pd

# 1
friends = pd.read_excel(r"C:\Users\hp\sowjanya_2026\friend_names.xls file.xlsx")
print("\nFriends:\n", friends)

# 2
family = pd.read_excel(r"C:\Users\hp\sowjanya_2026\family_members.xls file.xlsx")
print("\nFamily:\n", family)

# 3
veg = pd.read_excel(r"C:\Users\hp\sowjanya_2026\Vegfood_items.xlsx file.xlsx")
print("\nVeg Food:\n", veg)

# 4
nonveg = pd.read_excel(r"C:\Users\hp\sowjanya_2026\NonVegfood_items.xlsx file.xlsx")
print("\nNon-Veg Food:\n", nonveg)

# 5
months = pd.read_excel(r"C:\Users\hp\sowjanya_2026\month_names.xlsx file.xlsx")
print("\nMonths:\n", months)

# 6
colours = pd.read_excel(r"C:\Users\hp\sowjanya_2026\colours_names.xlsx file.xlsx")
print("\nColours:\n", colours)