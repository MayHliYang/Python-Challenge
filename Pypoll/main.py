import csv

# Path to the CSV file
file_path = 'election_data.csv'

# Initialize variables
total_votes = 0
candidates = {}

# Read the CSV file
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header

    # Process each row
    for row in reader:
        voter_id, county, candidate = row
        total_votes += 1
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Determine the winner and calculate percentages
winner = None
max_votes = 0
for candidate, votes in candidates.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate
    percentage = (votes / total_votes) * 100
    candidates[candidate] = (votes, percentage)

# Print results to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, data in candidates.items():
    votes, percentage = data
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write results to a text file
with open('election_results.txt', mode='w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, data in candidates.items():
        votes, percentage = data
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
