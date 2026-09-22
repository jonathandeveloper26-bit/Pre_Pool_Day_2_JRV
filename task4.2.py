
def calculate_pi(num_refinements, iteration=0):
  if iteration >= num_refinements:
    return 0
  else:
    return ((2*iteration + 1) **2)/(6+calculate_pi(num_refinements,iteration+1))


num_digits = int(input("Enter the Number of Digits: "))
num_refinements = int(input("Enter the Number of Refinements: "))

pi_estimate = 3 + calculate_pi(num_refinements)
print(f"(Approximation of pi: {pi_estimate:.{num_digits}f}")
