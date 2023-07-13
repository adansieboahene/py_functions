P = 10000
n = 12
r = 0.08

def calculate_compound_interest(P, n, r, t):
  amount = P * (1 + r / n) ** (n * t)
  return amount

t = float(input("Enter the number of years: "))

final_amount = calculate_compound_interest(P, n, r, t)

print("The final amount is:", final_amount)