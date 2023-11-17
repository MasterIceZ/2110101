import os

tests = 6

for test_idx in range(1, tests+1):
  print(f"===== trying {test_idx} =====")
  print(f"===== your output=====")
  os.system(f"python3 apec.py < {test_idx}.in")
  print(f"===== sol output=====")
  os.system(f"cat {test_idx}.out")