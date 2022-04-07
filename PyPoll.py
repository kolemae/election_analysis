# The data we need to retrieve -- Resources\election_results.csv
# 1. Total number of votes cast
# 2. Complete list of candidates who received votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candidate won
# 5. Winner of election based on popular vote

# Add dependencies
import csv
import os

# Assign variable to load file from a path
load_file = os.path.join("Resources", "election_results.csv")

# Assign variable to save the file to a path
save_file = os.path.join("Analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0

# Candidate options and votes
candidate_options = []
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open election results and read file
with open(load_file) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read header row
    headers = next(file_reader)

    # Print each row in CSV file
    for row in file_reader:
        # Add to total vote coeunt
        total_votes += 1

        # Print candidate name from each row
        candidate_name = row[2]

        # If candidate does not match existing candidate
        if candidate_name not in candidate_options:

            # Add to list of candidates
            candidate_options.append(candidate_name)

            # Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add votes to candidate's count
        candidate_votes[candidate_name] += 1

# Determine percentage of votes for each candidate
# Go through candidate list
for candidate_name in candidate_votes:

    # Retrieve vote count for candidate
    votes =  candidate_votes[candidate_name]

    # Calculate percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    # Print candidate name, vote count, and percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if votes are greater than winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"------------------------------\n")
print(winning_candidate_summary)

# Use with statement to open file as text file
with open(save_file, "w") as txt_file:
    # Write counties to the file with header
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
