print(f'''{'='*43}
CONVERSOR DE BASE DECIMAL PARA BASE BINÁRIA
{'='*43}''')

#Conversor de bases (Decimal → Binário).
while True:
  dividendo = float(input("\nDigite um número e ele será convertido em BINÁRIO: "))
  n_informado = dividendo
  quociente = 1
  lista = []

  while quociente >= 1:
    resto = dividendo%2
    lista.insert(0,resto)
    quociente = dividendo // 2
    dividendo = quociente

  binario = ''.join([str(item) for item in lista])
  print("O número  →", n_informado, "←  vale  →", binario, '←  em binário!')

#Confirmação se o usário deseja que a aplicação continue.
  resposta = input('\nDeseja continuar? [S/N] ').upper()[0]
  while resposta != 'S' and resposta != 'N':
    resposta = input('Resposta invalida, use [S] ou [N]. ').upper()[0]
  if resposta == 'N':
    break
    
#Resposta ao finalizar a aplicação.
print('''
Volte sempre! :D''')

print(f'''
{'='*32}
Alunos:
Daniel Ferreira - 01504933
Everton Figueirôa - 01177129
Matheus Victor - 01515370
Vinicius Rodrigues - 01519574
{'='*32}''')
