"""O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
 Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""
aluno1 = str(input('Primeiro aluno:'))
aluno2 = str(input('Segundo aluno:'))
aluno3 = str(input('Terceiro aluno'))
aluno4 = str(input('Quarto aluno'))
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
def sortearApresentacao(lista_alunos):
    print(f'Apresentação será nessa ordem:{sorted(lista_alunos)}')
    return sorted(lista_alunos)

sortearApresentacao(lista_alunos)