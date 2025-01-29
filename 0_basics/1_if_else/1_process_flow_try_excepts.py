try:
  # len(3) # TypeError
  # 0/0 # ZeroDivisionError
  print('hello')

except TypeError:
  print('Ocorreu erro de tipo')
except ZeroDivisionError as e:
  print('O erro recebido:', e)
except:
  print('Erro genérico')
else:
  print('Caso tenha passado sem erro, executa isso')
finally:
  print('Vem aqui sempre.')