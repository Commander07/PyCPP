import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
  name="PyCPP",
  version="0.0.5",
  author="Commander07",
  author_email="author@example.com",
  description="PyCPP is a simple tool for wrapping and using C++ functions and libraries.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/commander07/PyCPP",
  packages=setuptools.find_packages(),
  python_requires='>=3.6',
  scripts=['bin/pycpp.py']
)
