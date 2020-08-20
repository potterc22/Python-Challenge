import os
import csv

#declare variables
total_months = 0
net_amount = 0
# Use change_amounts to hold the change amounts between each month
change_amounts = []
greatest_inc = 0
greatest_dec = 0
profit_loss_change = 0
# we have to set previous_profit_loss to 0 for the first line when calculating profit/loss change
previous_profit_loss = 0
    
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
        net_amount += int(row[1])
        # calculate profit/loss change
        profit_loss_change = int(row[1]) - previous_profit_loss
        # set previous_profit_loss to the current profit/losses to help us calculate the change for the next row
        previous_profit_loss = int(row[1])        
        # add each profit/loss change amount to the change amounts list
        change_amounts.append(profit_loss_change)
        # use an if statement to find greatest increase and decrease
        if profit_loss_change > greatest_inc:
            greatest_inc = profit_loss_change
            # create variable for greatest increase month
            increase_month = row[0]
        elif profit_loss_change < greatest_dec:
            greatest_dec = profit_loss_change
            # create variable for greatest decrease month 
            decrease_month = row[0]
        # if the profit/loss change is not > greatest increase and not < greatest decrease, we want to continue to the next row
        else:
            continue
    # Use change_amounts list to calculate average change
    avg_change = round(sum(change_amounts) / len(change_amounts),2)

        
        
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {increase_month} (${greatest_inc})")
print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_dec})")

# specify the file to write our output to
ouput_path = os.path.join("Analysis", "analysis.csv")
# create function that prints out analysis to use for writerow
#def print_analysis()
# Open the file using "write" mode
with open(ouput_path, 'w') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter = ',')
    # Write the rows
    csvfile.write("Financial Analysis\n")
    csvfile.write("---------------------------\n")
    csvfile.write(f"Total Months: {total_months}\n")
    csvfile.write(f"Total: ${net_amount}\n")
    csvfile.write(f"Average Change: ${avg_change}\n")
    csvfile.write(f"Greatest Increase in Profits: {increase_month} (${greatest_inc})\n")
    csvfile.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_dec})\n")
    csvfile.write("---------------------------")
