x = input().split()
a = int(x[0])
b = int(x[1])
preco = [4.00,4.50,5.00,2.00,1.50]
total = preco[a-1]*b
print("Total: R$ {:.2f}".format(total))