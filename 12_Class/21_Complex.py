class Complex:
  integer = 0
  imaginary = 0

  def __init__(self, a, b):
    self.integer = a
    self.imaginary = b
  
  def __str__(self):
    res = ""
    if self.integer != 0:
      res += str(self.integer)
    if self.imaginary < 0:
      res += str(self.imaginary) + "i"
    if self.imaginary > 0:
      res += "+" + str(self.imaginary) + "i"
    return res

  def __add__(self, rhs):
    res = Complex(self.integer + rhs.integer, self.imaginary + rhs.imaginary)
    return res

  def __mul__(self, rhs):
    res = Complex(self.integer * rhs.integer - self.imaginary * rhs.imaginary, )