from utils_log import log_decorator
from simple_decorator import simple_decorator

@log_decorator
@simple_decorator
def somar(x, y):
    return x + y

if __name__ == '__main__':
    try:
        somar(2, 3)
        somar(2, '3')
        somar(10, 15)
    except:
        print("Esse decorator não atrapalha o erro")