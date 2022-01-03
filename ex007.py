titulo = ('MÉDIA XXX')
print('*'*40)
print('{:^40}'.format(titulo))
print('*'*40)
print('')

print('Informe as notas duas notas do aluno.')
nome = str(input('Informe o nome do aluno: '))
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
med = (n1 + n2)/2

print('')
print('''
O aluno {}
Obteve {} no primeiro semestre e {} no segundo semestre.
Ficando com a média {}.
'''.format(nome, n1, n2, med))

if med >= 8:
    print('O aluno {} foi aprovado com média A. Parabéns!!!'.format(nome))

elif (med >= 6) and (med < 8):
    print('O aluno {} foi aprovado com média B. Se esforçar mais, conseguirá média A...'.format(nome))

else:
    print('O aluno {} foi reprovado. Precisa estudar mais...'.format(nome))