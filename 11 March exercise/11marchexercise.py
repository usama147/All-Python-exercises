Basic_salary = 1500
Bonus_rate = 200
Commision_rate = 0.02

Number_of_laptops = int(input("Insert number of laptops"))
Price_of_laptops = int(input("Insert price of laptop"))

Bonus = (Bonus_rate * Number_of_laptops)
print(Bonus)
Commision_rate = (Commision_rate * Number_of_laptops * Price_of_laptops)
print(Commision_rate)
Gross_salary = (Basic_salary + Commision_rate + Bonus)
print(Gross_salary)
