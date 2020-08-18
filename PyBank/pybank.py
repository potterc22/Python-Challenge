import os
import csv

#declare variables
total_months = 0
net_amount = 0
# Use change_amounts to hold the change amounts between each month
change_amounts = []
greatest_inc = 0
greatest_dec = 0
# Use change_amounts list to calculate average change
avg_change = sum(change_amounts) / len(change_amounts)

    
# Path to collect data from the Resources folder
pybank_csv = os.path.join("Resources", "budget_data.csv")

with open (pybank_csv) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')
    # Read the header row first 
    csv_header = next(csvreader)
    # Loop through the rows 
    for row in csvreader:
        # for each row we will add one to the total_months variable
        total_months += 1
        # for each row we are adding the Profit/losses amount to the net_amount variable
        net_amount += row[1]
        for row + 1 in csvreader:
            change_amounts.append((row + 1) - row)
        
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {net_amount}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: (${greatest_inc})")
print(f"Greatest Decrease in Profits: (${greatest_dec})")

