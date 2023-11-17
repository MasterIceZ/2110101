# Run length encoding
# จงเขียนฟังก์ชั่นบีบอัดข้อความสาย DNA ที่มีแค่ ATCG (ตัวใหญ่หรือตัวเล็กก็ได้) เท่านั้น

def encode(inputstring):
# encode จะบีบอัดข้อความ (string) โดยนับจำนวนตัวอักษรที่ติดกันและแทนด้วยตัวเลข
# รับข้อมูลเป็น string ที่ประกอบด้วย ATCG (ตัวใหญ่หรือตัวเล็กก็ได้)
# และคืนค่าเป็น string ที่เป็นตัวใหญ่และตัวเลขเท่านั้น
# ถ้าข้อมูล inputstring ไม่ถูกต้องให้คืนว่า "ERROR"
# ตัวอย่าง
# "AAAA" -> "A4"
# "aAAACTGG" -> "A4CTG2"
# "CATS" -> "ERROR"
  outputstring = ""
  for x in inputstring.upper():
    if x not in "ATCG": 
      return "ERROR"
  last_char = inputstring[0].upper()
  cnt = 1
  for x in inputstring[1:].upper():
    if x == last_char:
      cnt += 1
    else:
      if cnt > 1:
        outputstring += last_char + str(cnt)
      else:
        outputstring += last_char
      cnt = 1
    last_char = x
  if cnt > 1:
    outputstring += last_char + str(cnt)
  else:
    outputstring += last_char
  # print(inputstring, outputstring)
  return outputstring


def decode(inputstring):
# decode จะย้อนกลับกระบวนการของ encode
# รับข้อมูลเป็น string ที่ประกอบด้วย ATCG และตัวเลข (ตัวใหญ่หรือตัวเล็กก็ได้)
# และคืนค่าเป็น string ที่เป็นตัวใหญ่ ATCG เท่านั้น
# ถ้าข้อมูล inputstring ไม่ถูกต้องให้คืนว่า "ERROR"
# ตัวอย่าง
# "A4" -> "AAAA"
# "AAC4G" -> "ERROR" (ไม่ควรมี AA ติดกันจากกระบวนการ encode)
# "a4CtG2" -> "AAAACTGG"
# "ERROR" -> "ERROR"
  outputstring = ""
# parse inputstring
  l = list()
  i = 0
  if inputstring == "ERROR" or inputstring == "": return "ERROR"
  while i < len(inputstring):
    if inputstring[i].isalpha() and inputstring[i].isupper():
      l.append(inputstring[i])
      i += 1
      if i < len(inputstring) and not inputstring[i].isnumeric():
        l.append(1)
      if i == len(inputstring):
        l.append(1)
    elif inputstring[i].isnumeric():
      c = 0
      while i < len(inputstring) and inputstring[i].isnumeric() :
        c *= 10
        c += int(inputstring[i])
        i += 1
      l.append(int(c))
    else:
      return "ERROR"
  # print(l)
  for i in range(0, len(l), 2):
    outputstring += l[i] * l[i + 1]
  # print(outputstring)
  return outputstring

#ให้เขียน test case สำหรับทดสอบคำสั่ง encode และ decode อย่างละ 10 test case
# เราจะใช้คำสั่ง assert https://www.w3schools.com/python/ref_keyword_assert.asp
#ตัวอย่างการใช้งาน
# assert encode("CATS") == "ERROR" #ตอน function เปล่าๆ บรรทัดนี้จะไม่เกิดอะไรขึ้น
# assert encode("AAAA") == "A4"
# assert decode("") == "asdf" #เมื่อปรับ function แล้ว บรรทัดนี้จะเกิด AssertionError

# เขียน test case encode สิบอันด้านล่าง
assert encode("CATS") == "ERROR"
assert encode("AAAA") == "A4"
assert encode("aAAACTGG") == "A4CTG2"
assert encode("123ew232323") == "ERROR"
assert encode("CTCTCTCTCTCATCG") == "CTCTCTCTCTCATCG"
assert encode("A") == "A"
assert encode("A"*100) == "A100"
assert encode("B"*100) == "ERROR"
assert encode("ATCG") == "ATCG"
assert encode("GGTCGCG") == "G2TCGCG"

# เขียน test case decode สิบอันด้านล่าง
# assert decode("CTCTCTCTCTCATCG") == "CTCTCTCTCTCATCG"
# assert decode("A4") == "AAAA"
assert decode("a1t2c3g4") == "ERROR"
assert decode("ERROR") == "ERROR"
assert decode("T120") == "T" * 120
assert decode("AT2C3G4") == "ATTCCCGGGG"
assert decode("A10") == "AAAAAAAAAA"
assert decode("A") == "A"
assert decode("T300A29") == "T" * 300 + "A" * 29
assert decode("") == "ERROR"
assert decode("aattccgg") == "ERROR"
assert decode("A14T232C81G12") == "A" * 14 + 232 * "T" + "C" * 81 + "G" * 12