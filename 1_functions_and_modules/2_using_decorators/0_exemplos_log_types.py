from loguru import logger

logger.debug('Uma mensagem para o desenvolvedor, só vai ver isso durante o desenvolvimento :D')
logger.info('Normalmente vai usar isso pra dar uma informação sobre a aplicação, por exemplo tempo de execução.')
logger.warning('Um aviso, algo que é importante, mas não crítico')
logger.error('Aconteceu uma falha, entrou em algum except')
logger.critical('Aconteceu uma falha que aborta a aplicação, algum erro mais grave ou não mapeado.')
