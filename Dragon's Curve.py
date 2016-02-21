def Dragon(n):
  mapping = {'a': 'aRbFR', 'b': 'LFaLb'}

  D0 = 'Fa'
  i = 0
  while i < n:
    D0 = D0.translate(mapping)
    i += 1
         
  print D0
  return ''.join([c for c in D0 if c.isupper()])


print (Dragon(1))