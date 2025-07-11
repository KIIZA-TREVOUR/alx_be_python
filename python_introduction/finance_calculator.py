# finance_calculator.py

# User Input
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are: ${monthly_savings}.")

# Project Annual Savings with 5% interest
yearly_savings = monthly_savings * 12
interest = yearly_savings * 0.05
projected_savings = yearly_savings + interest

# Output
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")
