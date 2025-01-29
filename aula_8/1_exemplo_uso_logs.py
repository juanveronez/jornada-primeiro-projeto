from loguru import logger
from sys import stderr

# Removendo os handlers existentes para evitar duplicação
logger.remove()

# Exemplo básico de arquivo de logs (com format padrão)
logger.add('logs/all_logs.log')

# Configuração do logger para stderr (execução no terminal)
logger.add(
            sink=stderr,
            format="{time} <r>{level}</r> <g>{message}</g> {file}",
            level="INFO"
          )

# Configuração do logger para arquivo de log
logger.add(
            "logs/critical_logs.log",
            format="{time} {level} {message} {file}",
            level="CRITICAL"
          )

# print -> logger.info
def somar(x, y):
  try:
    soma = x + y
    logger.info(f'Soma realizada: {x} + {y} = {soma}')

    return soma
  except:
    logger.critical("Os valores digitados não são validos.")


somar(2, 3)
somar(2, '3')
somar(10, 15)