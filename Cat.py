"""
The cat command will print the output of any file to the output stream. Currently working on printing the output of any file to another file when given such file name as input.
"""

def cat(**kwargs):
  params = kwargs.get("params", None)
  #flags = kwargs.get("flags", None)
  results = ""
  files = params[0:]
  for file in files:
    with open(file) as f:
      data = f.read()
      results += data
  print(results)

  #return results


if __name__=='__main__':
  # res = cat(['main.py','random.txt'])
  # print(res)
  cat(params = ['random.txt', 'main.py'])