# Election Analysis
Used Python to perform an election audit using a CSV file of election data.

## Table of contents
* [Overview of Election Audit](#overview-of-election-audit)
* [Resources](#resources)
* [Election Audit Results](#election-audit-results)
* [Summary](#summary)

## Overview of Election Audit
I assisted a Colorado Board of Elections employee to audit US Congressional election results. We used Python to retrieve the following data from a CSV file and saved it to a text file:

1. Total number of votes cast
2. A list of counties
3. Percentage of votes in each county
4. Number of votes in each county
5. The county with largest turnout
6. A list of candidates
7. Percentage of votes won by each candidate
8. Number of votes won by each candidate
9. The election winner based on popular vote

### Resources
- Data source: election_results.csv
- Software: Python ActivePython 3.7.8, Visual Studio Code 1.66.0

## Election Audit Results
The audit covered the following area with white fill.

![Audit Map](/Resources/audit_map.png)

- Total votes cast: 369,711
- County votes:
  - Jefferson County had 38,855 votes and 10.5% of the total votes
  - Denver County had 306,055 votes and 82.8% of the total votes
  - Arapahoe County had 24,801 votes and 6.7% of the total votes
- Denver County had the largest number of votes
- Candidate votes:
  - Charles Casper Stockham had 85,213 votes and 23.0% of the total votes
  - Diana DeGette had 272,892 votes and 73.8% of the total votes
  - Raymon Anthony Doane had 11,606 votes and 3.1% of the total votes
- **The election winner was Diana DeGette**

![Election Results](/Resources/final_results.png)

## Summary
I propose that the election commission use and modify this code as needed for other elections. With minor changes it can:

1. Be scaled down to analyze municipal government elections
2. Be scaled up from counties to states or evaluating additional districts
3. Include additional data, like affiliated party or voter demographics
4. Count and calculate by voting method (mail-in ballot, punch card, or direct recording electronic)

![Code to Edit](/Resources/code_to_edit.png)

- To scale down or up edit `#1` and the following `list` and `dictionary` to reflect the desired measurement
- Don't forget to check `#2` and change the `string` and `variable` as needed
- Under the `for row in reader:` loop make sure the `row[]` in the `load_file` matches the desired data to extract
- For additional data or calculations some code may be copy-pasted and edited within the [PyPoll_Challenge](Resources/PyPoll_Challenge.py) file to fit desired analysis


