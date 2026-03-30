# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:24:19 2026

@author: hp
"""

import pandas as pd

# 1. Friend Names CSV
friends = pd.read_csv(r"C:\Users\hp\sowjanya_2026\friend_names.csv file.txt")
print("\nFriends Data:\n", friends)

# 2. Family Members (* delimiter)
family = pd.read_csv(r"C:\Users\hp\sowjanya_2026\family_members.txt file.txt", delimiter="*")
print("\nFamily Data:\n", family)

# 3. Veg Food (| delimiter)
veg = pd.read_csv(r"C:\Users\hp\sowjanya_2026\vegfood_items.txt file.txt", delimiter="|")
print("\nVeg Food Data:\n", veg)

# 4. Non-Veg Food (| delimiter)
nonveg = pd.read_csv(r"C:\Users\hp\sowjanya_2026\nonvegfood_items.txt file.txt", delimiter="|")
print("\nNon-Veg Food Data:\n", nonveg)

# 5. Months (& delimiter)
months = pd.read_csv(r"C:\Users\hp\sowjanya_2026\month_names.txt file.txt", delimiter="&")
print("\nMonths Data:\n", months)

# 6. Colours (^ delimiter)
colours = pd.read_csv(r"C:\Users\hp\sowjanya_2026\colours_names.txt file.txt", delimiter="^")
print("\nColours Data:\n", colours)