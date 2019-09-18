from math import sqrt
n = input().split()
a = float(n[0]);
b = float(n[1]);
c = float(n[2]);

delta = (b**2) - (4*a*c);

if delta <= 0 or a <= 0:
    print("Impossivel calcular")

else:
    delta = sqrt(delta)
    x1 = (- b + delta) / (2 * a);
    x2 = (- b - delta) / (2 * a);
    print("R1 = {:.5f}\nR2 = {:.5f}".format(x1, x2))