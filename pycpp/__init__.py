import ctypes
import os
from shutil import copy
try:
  from . import FuncParser
except ImportError:
  import FuncParser


def loadDLL(dll):
  c_lib = ctypes.CDLL(os.getcwd() + "/" + dll + ".dll")
  funcs = FuncParser.parse(os.getcwd() + "/" + '/'.join(dll.split("/")[:-1]) + "/src/" + dll.split("/")[-1] + ".cpp")
  return c_lib, funcs


def wrap(dll, out):
  c_lib, funcs = loadDLL(dll)
  code = []
  for ff in funcs:
    f_code = "def {{name}}({{*arg}}):\n\tc_lib.{{name}}.restype = {{res}}\n\treturn c_lib.cmult({{*arg_}})"
    star_arg = ""
    star_arg_ = ""
    i = 0
    f_code = f_code.replace("{{name}}", ff.name).replace("{{res}}", "ctypes." + str(ff.restype))
    for key in ff.args:
      star_arg += key + ", "
      star_arg_ += "ctypes." + str(ff.args[key]) + "(" + key + "), "
      i += 1
    f_code = f_code.replace("{{*arg}}", star_arg[:-2]).replace("{{*arg_}}", star_arg_[:-2])
    code.append(f_code)
  if not os.path.exists(os.getcwd() + "/" + out + "/" + dll.split("/")[-1]):
    os.makedirs(os.getcwd() + "/" + out + "/" + dll.split("/")[-1])
  file = open(os.getcwd() + "/" +out + "/" + dll.split("/")[-1] + "/__init__.py", "w")
  file.write("")
  file.close()
  file = open(os.getcwd() + "/" + out + "/" + dll.split("/")[-1] + "/__init__.py", "a")
  file.write('import ctypes,os\nlib_name = os.path.realpath(__file__).replace("__init__.py", "dllmain.dll")\nc_lib = ctypes.CDLL(lib_name)\n')
  for d in code:
    file.write(d)
    # exec(d, globals())
  file.close()
  copy(os.getcwd() + "/" + dll + ".dll", os.getcwd() + "/" +out + "/" + dll.split("/")[-1] + "/" + dll.split("/")[-1] + ".dll")
  return code
