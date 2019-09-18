from math import trunc
N = float(input())
v = N;
n100 = trunc(N/100);
N %= 100;
n50 = trunc(N / 50);
N %= 50;
n20 = trunc(N / 20);
N %= 20;
n10 = trunc(N / 10);
N %= 10;
n5 = trunc(N / 5);
N %= 5;
n2 = trunc(N / 2);
N %= 2;

cents = N * 100;

m1 = trunc(cents / 100);
cents %= 100;
m050 = trunc(cents/50);
cents %= 50;
m025 = trunc(cents/25);
cents %= 25;
m010 = trunc(cents/10);
cents %= 10;
m05 = trunc(cents/5);
cents %= 5;
m01 = trunc(cents/1);





print("NOTAS:\n{} nota(s) de R$ 100.00\n{} nota(s) de R$ 50.00\n{} nota(s) de R$ 20.00\n{} nota(s) de R$ 10.00\n{} nota(s) de R$ 5.00\n{} nota(s) de R$ 2.00\nMOEDAS:\n{} moeda(s) de R$ 1.00\n{} moeda(s) de R$ 0.50\n{} moeda(s) de R$ 0.25\n{} moeda(s) de R$ 0.10\n{} moeda(s) de R$ 0.05\n{} moeda(s) de R$ 0.01".format(n100,n50,n20,n10,n5,n2,m1,m050,m025,m010,m05,m01))

