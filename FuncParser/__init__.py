import re


class func_:
  def __init__(self, restype, args, name):
    self.args = args
    self.restype = restype
    self.name = name


def parse(file):
  code = open(file).read().split("\n")
  between_args = "\\((.*)\\)"
  funcs = []
  define = False
  define_ = ""
  nextLineEqFunc = False
  for line in code:
    if line.startswith("#") or line.startswith("//"):
      if line.startswith("#define") and not define:
        define = True
        define_ = line.split(" ")[1]
      continue
    if nextLineEqFunc:
      fs = line.split(" ")
      args = {}
      args_ = re.findall(between_args, line)[0].split(", ")
      for arg in args_:
        arg_ = arg.split(" ")
        args[arg_[1]] = "c_" + arg_[0]
      name = fs[1].split("(")[0]
      res = "c_" + fs[0]
      funcs.append(func_(res, args, name))
    if line == define_ and define:
      nextLineEqFunc = True
      continue
    else:
      nextLineEqFunc = False
  return funcs
