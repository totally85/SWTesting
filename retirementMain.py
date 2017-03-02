import retirement

#take input from user
currentAge = int(input("What is your current age? "))
annualSalary = float(input("What is your annual salary? "))
percentSaved = (float(input("What percent of your salary are you putting into savings? ")) * 2) / 100 #employer matches savings so double amount entered then convert to decimal
savingsGoal = float(input("What is your retirement savings goal? "))

retirement.retirement(currentAge,annualSalary,percentSaved,savingsGoal)
