from functools import wraps

def simple_decorator(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    print('just a simple decorator function :D')
    result = func(*args, **kwargs)
    return result
    
  return wrapper
