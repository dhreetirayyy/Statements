actual_cost = float(input("Please Enter the Actual Price: "))
sale_amount = float(input("Please Enter the Sale Price: "))
if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit Earned!")
