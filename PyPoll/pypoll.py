import os
import csv

# Declare Variables
total_votes = 0
candidates = []
candidate_votes = {}
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
        # Find the unique list of Candidates who received votes and calculate each candidates vote amounts using a dictionary
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] = candidate_votes[row[2]] + 1


    # Print output to terminal
    print("Election Results")
    print("------------------------------")
    print(f'Total Votes: {total_votes}')
    print("------------------------------")
    for candidate in candidate_votes:
        # Declare vote_percentage variable that divides each candidates votes and divides them by the total votes
        vote_percentage = round(((candidate_votes[candidate]/total_votes)*100))
        # Declare vote_count
        vote_count = candidate_votes[candidate]
        print(f"{candidate}: {vote_percentage}% ({vote_count})")
    print("------------------------------")
    # found how to return first key in a dictionary using https://www.geeksforgeeks.org/python-get-the-first-key-in-dictionary/
    winner = list(candidate_votes.keys())[0]
    print(f'Winner: {winner}')
    print("------------------------------")

ouput_path = os.path.join("Analysis", "analysis.csv")

# Open the file using "write" mode
with open(ouput_path, 'w') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter = ',')
    # Write the output similar to how we print to terminal but using write instead of print
    csvfile.write("Election Results\n")
    csvfile.write("----------------------------\n")
    csvfile.write(f'Total Votes: {total_votes}\n')
    csvfile.write("----------------------------\n")
    for candidate in candidate_votes:
        # Declare vote_percentage variable that divides each candidates votes and divides them by the total votes
        vote_percentage = round(((candidate_votes[candidate]/total_votes)*100))
        # Declare vote_count
        vote_count = candidate_votes[candidate]
        csvfile.write(f"{candidate}: {vote_percentage}% ({vote_count})\n")
    csvfile.write("----------------------------\n")
    csvfile.write(f'Winner: {winner}\n')
    csvfile.write("----------------------------")