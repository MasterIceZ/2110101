class roman :
  def __init__(self, r):
    self.string = r

  def __lt__(self, rhs):
    return int(self) < int(rhs)
  
  def __str__(self):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res = ""
    it = 0
    n = int(self)
    while n > 0:
      for x in range(n // values[it]):
        res += symbols[it]
        n -= values[it]
      it += 1
    self.string = res
    return res
  
  def __int__(self):
    replace_list = [("IV", "IIII"), ("IX", "VIIII"), ("XL", "XXXX"), ("XC", "LXXXX"), ("CD", "CCCC"), ("CM", "DCCCC")]
    c = self.string
    for x in replace_list:
      c = c.replace(x[0], x[1])
    replace_list = [("I", "1 "), ("V", "5 "), ("X", "10 "), ("L", "50 "), ("C", "100 "), ("D", "500 "), ("M", "1000 ")]
    for x in replace_list:
      c = c.replace(x[0], x[1])
    return sum(map(int, c.split()))
  
  def __add__(self, rhs):
    return roman(str(int(self) + int(rhs)))

t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
# print(int(a), int(b))
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))