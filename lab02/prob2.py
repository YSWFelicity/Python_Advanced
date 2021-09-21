'''
Lab 1
Problem 1: Eating out with a group 
Yingshu Wang 
'''


def time_to_buy_house(cost_of_house, annual_salary, percent_salary_saved):
    down_payment = cost_of_house * 0.25
    monthly_savings = annual_salary * percent_salary_saved / 12 
    months_to_save = down_payment / monthly_savings 

    years = months_to_save // 12
    months = months_to_save % 12

    message = "If you save ${0:.2f} per month, it will take {1:.0f} year(s)" + \
        " and {2:.0f} month(s) to save enough for the down payment!"

    return message.format(monthly_savings, years, months)

# Test runs 
print(time_to_buy_house(100000, 50000, 0.25))

