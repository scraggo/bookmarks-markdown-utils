def replacer(arr, str):
  """Given list 'arr' of modifications,
  return str with specified modifications.
  params:
    arr: list of lists [string to find, string to replace with]
    str: string
  Caution - watch out for unicode chars. Ex: ' ' is unicode \xa0
  """
  for item in arr:
    str = str.replace(item[0], item[1])
  return str

def run_tests():
  # quick tests
  replacers = [
    ('<div> </div>', ''),
    ('<p></p>', ''),
    ('<div>', ''),
    ('</div>', '')
  ]
  # TEST 1
  s1 = '<div>{}</div>{}Testing!'.format(' ', '\n')
  t1 = replacer(
    [replacers[0]],
    s1
  )
  exp1 = '\nTesting!'
  assert exp1 == t1, t1
  # TEST 2
  s2 = '<div>{}</div>{}Testing!<p></p>P was here.<div></div>Div was here.'.format(' ', '\n')
  t2 = replacer(
    replacers[:],
    s2
  )
  exp2 = '\nTesting!P was here.Div was here.'
  assert exp2 == t2, t2
  print('all tests passed!')

def main():
  run_tests()

if __name__ == '__main__':
  main()
