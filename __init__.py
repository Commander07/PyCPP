import ctypes
import os
from . import FuncParser
lib_name = os.path.realpath(__file__).replace("__init__.py", "dllmain.dll")
c_lib = ctypes.CDLL(lib_name)
funcs = FuncParser.parse("pycpp/dll/dllmain.cpp")


# Example function
def cmult(x: int, y: float) -> float:
  c_lib.cmult.restype = ctypes.c_float
  return c_lib.cmult(x, ctypes.c_float(y))


def call(func, *args):
  f_code = "def {{name}}({{*arg}}):\nc_lib.{{name}}.restype = {{res}}\nreturn c_lib.cmult({{*arg_}})"
  f = getattr(c_lib, func)
  arg = []
  arg_ = []
  for ff in funcs:
    if ff.name == func:
      f.restype = ff.restype
      i = 0
      for key in ff.args:
        arg.append(ff.args[key](args[i]))
        arg.append("ctypes." + ff.args[key] + "(" + args[i] + ")")
        i += 1
      break
  f(*arg)
