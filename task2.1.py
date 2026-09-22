

for j in range(0,3):
  for pwr in range(2,6):
    print("\n")
    total_value = 0
    current_string = ""
    for i in range(0,9+j):
     current_string += "1"
     total_value += int(current_string)
     if i == 9+j-1:
       print(f"Additive Value: {total_value}\nExponential Value ({pwr}): {total_value ** pwr}")


