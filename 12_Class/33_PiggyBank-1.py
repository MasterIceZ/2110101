class piggybank:
 def __init__(self):
  # มีตัวแปร 4 ตัวเก็บจ านวนเหรียญของเหรียญแต่ละแบบ
  self.one = 0
  self.two = 0
  self.five = 0
  self.ten = 0

 def add1(self, n):
  # เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญบาท
  self.one += n

 def add2(self, n):
  # เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญสองบาท
  self.two += n

 def add5(self, n):
  # เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญห้าบาท
  self.five += n

 def add10(self, n):
  # เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญสิบบาท
  self.ten += n

 def __int__(self):
  # คืนมูลค่ารวม = ค่าของเหรียญคูณกับจ านวนเหรียญ
  return self.ten * 10 + self.five * 5 + self.two * 2 + self.one
 
 def __lt__(self, rhs):
  # เปรียบเทียบจ านวนเงินใน self กับจ านวนเงินใน rhs
  return int(self) < int(rhs)
 
 def __str__(self):
  # คืนสตริงที่แสดงจ านวนเหรียญแต่ละแบบตามตัวอย่าง
  return "{" + "1:{}, 2:{}, 5:{}, 10:{}".format(self.one, self.two, self.five, self.ten) + "}"

cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)