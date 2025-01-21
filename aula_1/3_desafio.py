# Calculo de Bonus com Entrada do Usuario
CONTANTE_BONUS = 1000

nome_usuario = input('Digite o seu nome: ')
salario_usuario = float(input('Digite o seu salário: '))
porcentagem_bonus = float(input('Digite o percentual de bônus: '))

valor_bonus = CONTANTE_BONUS + salario_usuario * porcentagem_bonus

print(f'Olá {nome_usuario}, o seu bônus foi de {valor_bonus}')
