import math

line = input().split(',')

all_decimals = int(line[1] + line[2])

non_repeat_decimals = int(line[1]) if len(line[1]) > 0 else 0

top_level = all_decimals - non_repeat_decimals

divider = int(("9" * len(line[2])) + ("0" * len(line[1])))

gcd = math.gcd(top_level, divider)

top_level //= gcd
divider //= gcd

print(int(line[0]) * divider + top_level, "/", divider)

