from math import trunc
tempo = int(input())
h = tempo//3600
rt = tempo - h *3600
m = rt//60
s = rt - m *60
print("{}:{}:{}".format(h,m,s))