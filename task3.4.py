
def extract_decimal(num):
  str_num = str(num)
  found_decimal = False
  decimal_digits = ""
  for char in str_num:
    if char == ".":
      found_decimal = True
      continue
    if(found_decimal):
      decimal_digits += char
  return decimal_digits

num1 = 12.24
num2 = 424242.8412


print(extract_decimal(num1))
print(extract_decimal(num2))
