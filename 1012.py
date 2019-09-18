d = input().split()
a = float(d[0])
b = float(d[1])
c = float(d[2])

tri = a*c/2
cir = 3.14159*(c*c)
tra = (a+b)/2 *c
qua = b*b
ret = a*b
print("TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}".format(tri, cir, tra, qua, ret))