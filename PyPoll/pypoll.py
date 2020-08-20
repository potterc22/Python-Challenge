import os
import csv

# Declare Variables
total_votes = 0
candidates = []
khan = 0
correy = 0
li = 0
otooley = 0
most_votes = 0

# Path to collect data from the Resources folder
pybank_csv = os.path.join("Resources", "election_data.csv")

with open (pybank_csv) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')
    # Read the header row first 
    csv_header = next(csvreader)
    # Loop through the rows 
    for row in csvreader:
        # Find the total votes by counting each row
        total_votes += 1
        # Find the unique list of Candidates who received votes
        if row[2] not in candidates:
            candidates.append(row[2])
        # Find the total number of votes each candidate won
        if row[2] == "Khan":
            khan += 1
        elif row[2] == "Correy":
            correy += 1
        elif row[2] == "Li":
            li += 1
        elif row[2] == "O'Tooley":
            otooley += 1
    # find the winnner:
    if khan > most_votes:
        most_votes = khan
        winner = "Khan"
    if correy > most_votes:
        most_votes = correy
        winner = "Correy"
    if li > most_votes:
        most_votes = li
        winner = "Li"
    if otooley > most_votes:
        most_votes = otooley
        winner = "O'Tooley"

# Declare vote percentage variables
khan_percentage = round((khan / total_votes) * 100,3)
correy_percentage = round((correy / total_votes) * 100,3)
li_percentage = round((li / total_votes) * 100,2)
otooley_percentage = round((otooley / total_votes) * 100,3)

print("Election Results")
print("------------------------------")
print(f'Total Votes: {total_votes}')
print("------------------------------")
print(f'Khan: {khan_percentage}% ({khan})')
print(f'Correy: {correy_percentage}% ({correy})')
print(f'Li: {li_percentage}% ({li})')
print(f"O'Tooley: {otooley_percentage}% ({otooley})")
print("------------------------------")
print(f'Winner: {winner}')
print("------------------------------")

ouput_path = os.path.join("Analysis", "analysis.csv")
# create function that prints out analysis to use for writerow
#def print_analysis()
# Open the file using "write" mode
with open(ouput_path, 'w') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter = ',')
    # Write the output
    csvfile.write("Election Results\n")
    csvfile.write("----------------------------\n")
    csvfile.write(f'Total Votes: {total_votes}\n')
    csvfile.write("----------------------------\n")
    csvfile.write(f'Khan: {khan_percentage}% ({khan})\n')
    csvfile.write(f'Correy: {correy_percentage}% ({correy})\n')
    csvfile.write(f'Li: {li_percentage}% ({li})\n')
    csvfile.write(f"O'Tooley: {otooley_percentage}% ({otooley})\n")
    csvfile.write("----------------------------\n")
    csvfile.write(f'Winner: {winner}\n')
    csvfile.write("----------------------------")