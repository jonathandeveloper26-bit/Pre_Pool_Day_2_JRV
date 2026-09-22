def sum_digits(num):
  val_to_string = str(num)
  sum_digits = 0
  for digit in val_to_string:
    sum_digits += int(digit)
  return sum_digits


value1 = 123456789
value2 = 112233445566778899
value3 = 123456789 * 987654321

print(sum_digits(value1))
print(sum_digits(value2))
print(sum_digits(value3))
