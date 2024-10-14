import numpy as np

vetor_alunos = np.empty (10, dtype=bytearray)

print(f'\nvetor_alunos: {vetor_alunos}')
print(f'\nTipo de estrutura do vetor_alunos: {type(vetor_alunos)}')

for n in range(3):
    vetor_alunos[n] = input(f'\nNome do {str(n+1)}º aluno(a):')

print(f'\nOs alunos(as) que entraram em sala são: {vetor_alunos} \n')