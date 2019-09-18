o = input().split()
a = int(o[0])
b = int(o[1])
c = int(o[2])

maiorAB = a
if b> a and b > c:
    maiorAB = b
if c > a and c > b:
    maiorAB = c

print("{} eh o maior".format(maiorAB))