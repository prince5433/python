import sys
from fractions import Fraction   # Exact fractions ke liye
from decimal import Decimal      # High precision decimals ke liye
ideal_temp=95.5
current_temp=95.49999999999999
print(f"Ideal temperature: {ideal_temp}")
print(f"Current temperature: {current_temp}")
print(f"Difference between ideal and current temperature: {ideal_temp - current_temp}")
print(sys.float_info)