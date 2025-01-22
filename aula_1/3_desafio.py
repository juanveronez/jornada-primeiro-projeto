### Desafio - Refatorar o projeto da aula anterior evitando Bugs!
CONSTANTE_BONUS = 1000

try:
  # 1) Solicita ao usuário que digite seu nome
  try:
    nome_usuario = input('Digite o seu nome: ')
    
    if len(nome_usuario) == 0:
      raise ValueError("O nome não pode estar vazio.")
    
    elif any(c.isdigit() for c in nome_usuario):
      raise ValueError("O nome não deve conter números.")
  
  except ValueError as e:
    print(e)
    exit()

  # 2) Solicita ao usuário que digite o valor do seu salário
  # Converte a entrada para um número de ponto flutuante
  try:
    salario_usuario = float(input('Digite o seu salário: '))
    
    if salario_usuario < 0:
      print("Por favor, digite um valor positivo para o salário.")
      exit()
  
  except ValueError as e:
    print('O salário deve ser um valor numérico')
    exit()

  # 3) Solicita ao usuário que digite o valor do bônus recebido
  # Converte a entrada para um número de ponto flutuante
  try:
    porcentagem_bonus = float(input('Digite o percentual de bônus: '))
    
    if porcentagem_bonus < 0:
      print("Por favor, digite um valor positivo para o percentual de bônus.")
      exit()
  
  except ValueError as e:
    print('O percentual de bônus deve ser um valor numérico')
    exit()

  # 4) Calcule o valor do bônus final
  valor_bonus = CONSTANTE_BONUS + salario_usuario * porcentagem_bonus
    
  # 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
  print(f'Olá {nome_usuario}, seu salário é R${salario_usuario:.2f} e seu bônus final é R${valor_bonus:.2f}.')
except KeyboardInterrupt:
  print('Processo finalizado de forma prematura.')
finally:
  print('Fim do desafio.')

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
