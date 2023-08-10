a = float(input())
b = float(input())
c = float(input())

x_1 = round((-b - (b ** 2 - 4.0 * a * c)**0.5) / (2.0 * a), 3)
x_2 = round((-b + (b ** 2 - 4.0 * a * c)**0.5) / (2.0 * a), 3)

print(f"{x_1} {x_2}")
