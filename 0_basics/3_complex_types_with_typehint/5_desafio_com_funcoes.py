### Desafio - Refatorar o projeto da aula anterior evitando Bugs!
CONSTANTE_BONUS: int = 1000

def solicita_nome():
  while True:
    try:
      nome_usuario: str = input('Digite o seu nome: ')
      
      if len(nome_usuario) == 0:
        raise ValueError("O nome não pode estar vazio.")
      
      elif any(c.isdigit() for c in nome_usuario):
        raise ValueError("O nome não deve conter números.")
      
      else:
        return nome_usuario
    except ValueError as e:
      print(e)

def solicita_salario():
  while True:
    try:
      salario_usuario: float = float(input('Digite o seu salário: '))
      
      if salario_usuario < 0:
        print("Por favor, digite um valor positivo para o salário.")
      else:
        return salario_usuario

    except ValueError:
      print('O salário deve ser um valor numérico')

def solicita_bonus():
  while True:
    try:
      porcentagem_bonus: float = float(input('Digite o percentual de bônus: '))
      
      if porcentagem_bonus < 0:
        print("Por favor, digite um valor positivo para o percentual de bônus.")

      else:
        return porcentagem_bonus

    except ValueError as e:
      print('O percentual de bônus deve ser um valor numérico')

def calcula_bonus(salario: float, bonus: float):
  valor_bonus: float = CONSTANTE_BONUS + salario * bonus
  return valor_bonus

def imprimi_mensagem_resultado(nome: str, salario: float, salario_com_bonus: float):
  print(f'Olá {nome}, seu salário é R${salario:.2f} e seu bônus final é R${salario_com_bonus:.2f}.')

def cria_funcionario():
  funcionario = {
    "nome": solicita_nome(),
    "salario": solicita_salario(),
    "bonus": solicita_bonus(),
  }

  salario_com_bonus = calcula_bonus(funcionario['salario'], funcionario['bonus'])
  imprimi_mensagem_resultado(funcionario['nome'], funcionario['salario'], salario_com_bonus)

  return funcionario

funcionarios = []
quer_sair = False
while quer_sair is not True:
  funcionario = cria_funcionario()
  funcionarios.append(funcionario)

  print(f'{len(funcionarios)} criado(s).')
  terminate = input('Fechar programa? (S ou N)')
  if terminate == 'S':
    quer_sair = True
