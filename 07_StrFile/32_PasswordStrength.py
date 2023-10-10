def no_lowercase(t): # return True if no lowercase, otherwise return False
  for x in t:
    if x.islower():
      return False
  return True
 
def no_uppercase(t):
  for x in t:
    if x.isupper():
      return False
  return True
 
def no_number(t):
  for x in t:
    if x.isdigit():
      return False
  return True
 
def no_symbol(t):
  for x in t:
    if not x.isalnum():
      return False
  return True
 
def character_repetition(t):
  t = t.lower()
  for i in range(len(t) - 3):
    for j in range(1, 4):
      if t[i + j] != t[i]:
        break
      if j == 3:
        return True
  return False

def number_sequence(t):
  s = "012345678901234"
  for i in range(len(t)-3):
    if t[i:i+4] in s or t[i:i+4] in s[::-1]:
      return True
  return False

def letter_sequence(t):
  s = "abcdefghijklmnopqrstuvwxyz"
  t = t.lower()
  for i in range(len(t)-3):
    if t[i:i+4] in s or t[i:i+4] in s[::-1]:
      return True
  return False

def keyboard_pattern(t):
  s = [
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm",
    "!@#$%^&*()_+"
  ]
  t = t.lower()
  for ss in s:
    for i in range(len(t)-3):
      if t[i:i+4] in ss or t[i:i+4] in ss[::-1]:
        return True
  return False
#-----------------------------
passw = input().strip()
errors = []
if len(passw) < 8:
  errors.append("Less than 8 characters")
if no_lowercase(passw):
  errors.append("No lowercase letters")
if no_uppercase(passw):
  errors.append("No uppercase letters")
if no_number(passw):
  errors.append("No numbers")
if no_symbol(passw):
  errors.append("No symbols")
if character_repetition(passw):
  errors.append("Character repetition")
if number_sequence(passw):
  errors.append("Number sequence")
if letter_sequence(passw):
  errors.append("Letter sequence")
if keyboard_pattern(passw):
  errors.append("Keyboard pattern")
if len(errors) == 0:
  print('OK')
else:
  print("\n".join(errors))