# Add dependencies.
import csv
import os

# Assign variable to load file from a path
load_file = os.path.join("Resources", "election_results.csv")

# Assign variable to save the file to a path
save_file = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0

# Candidate options and votes
candidate_options = []
candidate_votes = {}

# Winning candidate, vote count, and percentage
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

        # Add to total vote count
        total_votes += 1

        # Get candidate name from each row
        candidate_name = row[2]

        # If candidate does not match existing candidate
        if candidate_name not in candidate_options:

            # Add to candidate list
            candidate_options.append(candidate_name)

            # Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add votes to candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to text file
with open(save_file, "w") as txt_file:

    # Print the final vote count
    election_results = (
        f"\nElection Results\n"
        f"----------------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------------------------\n")

    print(election_results, end="")

    # Save final vote count to text file
    txt_file.write(election_results)
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print candidates' vote count and percentage
        print(candidate_results)

        #  Save candidate results to text file
        txt_file.write(candidate_results)

        # Determine winning vote count, percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print winning results
    winning_candidate_summary = (
        f"----------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------------------\n")

    print(winning_candidate_summary)
    
    # Save winning results to text file
    txt_file.write(winning_candidate_summary)