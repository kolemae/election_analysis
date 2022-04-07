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

# Open election results and read file
with open(load_file) as election_data:

        # Read file object with reader function
    file_reader = csv.reader(election_data)
    
    # Print header row
    headers = next(file_reader)
    print(headers)

# Use with statement to open file as text file
with open(save_file, "w") as txt_file:
    # Write counties to the file with header
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
