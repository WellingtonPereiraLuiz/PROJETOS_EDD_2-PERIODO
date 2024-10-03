def soma(n):
    somatorio = 0

    print(n)
    for i in range(len(n)):
        somatorio += n[i]
        if (n[i] % 2 == 0):
            print(f'\nO numero: {n[i]} é par')
        else:
            print(f'\nO numero: {n[i]} é impar')
        print(f'\nA soma de todos os valores é: {somatorio}')