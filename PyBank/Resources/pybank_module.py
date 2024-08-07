import os
import csv
budget_data = os.path.join("Resources","budget_data.csv")
# Open and read csv
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
 #Initialize variables for total months, total profit, and max and min profit
    total_months = 0
    total_profit_losses = 0
    # Read through each row of data after the header
    for row in csv_reader:
     total_months = total_months + 1
     #calculate total profit loss
     total_profit_losses = total_profit_losses + int(row[1])
# Print the results
print("Financial Analysis")
print("--------------------------")
print(f"total_months :{total_months}")
print(f"Total:${total_profit_losses}")









