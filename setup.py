import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
  name="PyCpp-Commander07",
  version="0.0.1",
  author="Example Author",
  author_email="author@example.com",
  description="A small example package",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/commander07/PyCPP",
  packages=setuptools.find_packages(),
  python_requires='>=3.6',
  scripts=['bin/pycpp']
)
