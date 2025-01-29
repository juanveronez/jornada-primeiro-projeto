from loguru import logger
from functools import wraps

# Removendo os handlers existentes para evitar duplicação
logger.remove()

logger.add(
            "logs/logs_de_info.log",
            format="{time} {level} {message} {file}",
            level="INFO"
          )

logger.add(
            "logs/logs_de_erros.log",
            format="{time} {level} {message} {file}",
            level="ERROR"
          )

def log_decorator(func):
    @wraps(func) # usado para criar um decorator de função, embrulhando a função com outra função para ser executada.
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando função '{func.__name__}' com args {args} e kwargs {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Função '{func.__name__}' retornou {result}")
            return result
        except Exception as e:
            logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
            raise  # Re-lança a exceção para não alterar o comportamento da função decorada
    return wrapper
