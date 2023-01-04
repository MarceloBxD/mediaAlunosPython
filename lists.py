import os

alunos = []
total_individual = '0.0'
continua_cadastro_notas = True

while continua_cadastro_notas:
    registro_aluno = {
        'nome': '',
        'notas': [],
        'media': 0.0
    }

    nome = input("Nome do aluno: ")
    nota = float(input("Nota do aluno: "))

    registro_aluno['nome'] = nome
    registro_aluno['notas'].append(nota)
    registro_aluno['media'] = sum(registro_aluno['notas']) / len(registro_aluno['notas'])

    print(registro_aluno)

    continua_cadastro_notas = input("Deseja continuar? (s/n) ")
    continua_cadastro_notas.capitalize()

    if continua_cadastro_notas == 'N':
        break
    else:
        os.system("clear")
        nome = input("Nome do aluno: ")
        nota = float(input("Nota do aluno: "))
        registro_aluno['nome'] = nome

        if nome in registro_aluno['nome']:
            registro_aluno['notas'].append(nota)
        else:
            registro_aluno['nome'] = nome
            registro_aluno['notas'].append(nota)
            registro_aluno['media'] = sum(registro_aluno['notas']) / len(registro_aluno['notas'])

os.system("clear")