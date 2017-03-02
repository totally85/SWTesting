#retirement

def retirement(currentAge, annualSalary, percentSaved, savingsGoal):
    #output what age savings goal will be met

    if (annualSalary * percentSaved) <= 0:
        print("Your savings goal will not be met.")
        return 100
    
    ageAtGoal = currentAge + savingsGoal / (annualSalary * percentSaved)


    if ageAtGoal >= 100:
        print("Your savings goal will not be met.")
        return 100

    else:
        print("You will meet your savings goal at age", ageAtGoal)
        return ageAtGoal
