p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))

si = (p * r * t) / 100
ci = p * (1 + r / 100) ** t - p

print("Simple Interest =", si)
print("Compound Interest =", ci)

