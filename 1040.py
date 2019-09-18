x = input().split()
n1 = float(x[0])
n2 = float(x[1])
n3 = float(x[2])
n4 = float(x[3])



for i in x:
    a += 1

if a < 4:
    media = ((n1*2) + (n2*3) + (n3*4) + (n4*1))/4
    if media >= 7:
        print("Aluno aprovado.")
    elif media >= 5 and media <= 6.9:
        print("Aluno em exame.")
    else:
        print("Aluno reprovado.")



