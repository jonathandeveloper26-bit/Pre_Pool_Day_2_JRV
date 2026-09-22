
def calculate_pi(num_digits, refinement):
  pi_est = 0
  for i in range(0, refinement+1):
    if i%2 == 0:
      pi_est += 4 * 1/(2*i+1)
    elif i%2 == 1:
      pi_est -= 4 * 1/(2*i+1)
  return round(pi_est,num_digits)

num_digits = int(input("Enter the number of digits to return: "))
refined = int(input("Enter the number of refinements: "))

print(calculate_pi(num_digits,refined))
