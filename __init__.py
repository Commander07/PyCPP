import ctypes, os
lib_name = os.path.realpath(__file__).replace("__init__.py", "cpp.dll")
c_lib = ctypes.CDLL(lib_name)
c_lib.cmult.restype = ctypes.c_float

# Example function
def cmult(x: int, y: float) -> float:
  return c_lib.cmult(x, ctypes.c_float(y))