def create_iterator(func, n):
  # TODO: Write code here to return a function 
  # that executes *func*, *n* times on a supplied input
  def newFunc(number):
    x = number
    n_ = n
    for i in range(n_):
        x = func(x)
    return x
  return newFunc

def get_double(n):
    return 2*n

df = create_iterator(get_double, 2)

print df(2)