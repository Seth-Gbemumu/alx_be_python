# Take the user's monthly income
monthly_income = int(input("Enter your monthly income: "))
# Take the user's monthly expenses
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are : ${monthly_savings}")
rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Projected savings after one year, with interest, is : ${projected_savings}."
