from math import trunc
N = int(input())
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
n1 = trunc(N);

print("{}\n{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n{} nota(s) de R$ 20,00\n{} nota(s) de R$ 10,00\n{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00\n{} nota(s) de R$ 1,00".format(v,n100,n50,n20,n10,n5,n2,n1))